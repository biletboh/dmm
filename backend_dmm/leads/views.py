from rest_framework import generics
from .serializers import LeadSerializer
from .models import Lead


class LeadListCreateView(generics.ListCreateAPIView):
    """Create and display a list of leads."""

    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
