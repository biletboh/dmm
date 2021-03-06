from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from rest_condition import Or

from .serializers import LeadSerializer, BriefSerializer, CommentSerializer
from .models import Brief, Lead
from .permissions import IsPostRequest, IsOptionsRequest


class LeadListCreateView(generics.ListCreateAPIView):
    """Create a lead and display a list of leads."""

    permission_classes = [Or(IsAuthenticated, IsPostRequest)]
    queryset = Lead.objects.all().order_by('-date')
    serializer_class = LeadSerializer


class LeadCommentView(generics.UpdateAPIView):
    """Create a lead and display a list of leads."""

    permission_classes = (IsAuthenticated,)
    queryset = Lead.objects.all()
    serializer_class = CommentSerializer


class BriefListCreateView(generics.ListCreateAPIView):
    """Create a brief and display a list of briefs."""

    permission_classes = [Or(IsAuthenticated, IsPostRequest, IsOptionsRequest)]
    queryset = Brief.objects.all()
    serializer_class = BriefSerializer
