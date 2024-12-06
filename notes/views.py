from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer

class NoteListCreateAPIView(APIView):
    def get(self, request):
        """Fetch all notes"""
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Handle create, update, and delete actions"""
        action = request.data.get('action', None)

        if not action:
            return Response(
                {"error": "Action is required in the request data."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if action == 'create':  # Create a new note
            return self._create_note(request)

        elif action == 'update':  # Update an existing note
            return self._update_note(request)

        elif action == 'delete':  # Delete an existing note
            return self._delete_note(request)

        return Response(
            {"error": f"Invalid action '{action}' provided. Allowed actions are: create, update, delete."},
            status=status.HTTP_400_BAD_REQUEST
        )

    def _create_note(self, request):
        """Private method to handle note creation"""
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _update_note(self, request):
        """Private method to handle note updating"""
        note_id = request.data.get('id')
        if not note_id:
            return Response({"error": "Note ID is required for update."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            note = Note.objects.get(id=note_id)
        except Note.DoesNotExist:
            return Response({"error": "Note not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = NoteSerializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _delete_note(self, request):
        """Private method to handle note deletion"""
        note_id = request.data.get('id')
        if not note_id:
            return Response({"error": "Note ID is required for deletion."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            note = Note.objects.get(id=note_id)
            note.delete()
            return Response({"message": "Note deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Note.DoesNotExist:
            return Response({"error": "Note not found."}, status=status.HTTP_404_NOT_FOUND)
