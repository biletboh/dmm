from rest_framework import generics
from .serializers import LeadSerializer, BriefSerializer
from .models import Brief, Lead


class LeadListCreateView(generics.ListCreateAPIView):
    """Create a lead and display a list of leads."""

    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class BriefListCreateView(generics.ListCreateAPIView):
    """Create a brief and display a list of briefs."""

    queryset = Brief.objects.all()
    serializer_class = BriefSerializer
