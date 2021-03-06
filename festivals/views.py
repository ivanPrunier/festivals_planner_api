from rest_framework import viewsets, permissions

from festivals.models import Artist, Festival, Show, Participation, Attendance, Party, Task, \
    PartyInvite

from festivals.serializers import FestivalSerializer, ArtistSerializer, ShowSerializer, \
    ParticipationSerializer, AttendanceSerializer, PartySerializer, TaskSerializer, \
    PartyInviteSerializer


class ArtistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ShowViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    permission_classes = (permissions.IsAuthenticated,)


class FestivalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ParticipationViewSet(viewsets.ModelViewSet):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    permission_classes = (permissions.IsAuthenticated,)


class PartyInviteViewSet(viewsets.ModelViewSet):
    queryset = PartyInvite.objects.all()
    serializer_class = PartyInviteSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)
