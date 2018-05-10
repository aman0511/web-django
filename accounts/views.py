from django.contrib.auth import get_user_model

from rest_framework import generics, views, response, filters
from rest_framework_csv.renderers import CSVRenderer

from . import serializers as acc_serializer
from . import messages as acc_messages

User = get_user_model()


class UserListCreateAPiView(generics.ListCreateAPIView):
    """
        User create and listing view
    """
    pagination_class = None

    serializer_class = acc_serializer.UserListingSerializer
    model = User
    queryset = User.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'first_name',)


class UserDetailApiView(generics.RetrieveAPIView):
    """ user details api view """

    serializer_class = acc_serializer.UserListingSerializer
    model = User
    queryset = User.objects.all()


class DeleteUser(views.APIView):
    """ delete multiple user """
    serializer_class = acc_serializer.UserDeleteSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            users = serializer.validated_data['users']
            User.objects.filter(id__in=[user.id for user in users]).delete()
            return response.Response({'detail':acc_messages.USER_DELETE_MESSAGE_RESPONSE_TEXT})


class DeActivateUser(views.APIView):
    """ delete multiple user """
    serializer_class = acc_serializer.UserDeActivateSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            users = serializer.validated_data['users']
            User.objects.filter(id__in=[user.id for user in users]).update(is_active=False)
            serializer = acc_serializer.UserListingSerializer(instance=users, many=True)
            return response.Response(serializer.data)


class ActivateUser(views.APIView):
    """ delete multiple user """
    serializer_class = acc_serializer.UserActivateSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            users = serializer.validated_data['users']
            User.objects.filter(id__in=[user.id for user in users]).update(is_active=True)
            users = User.objects.filter(id__in=[user.id for user in users])
            serializer = acc_serializer.UserListingSerializer(instance=users, many=True)
            return response.Response(serializer.data)


class  UserCsvDownLoad(views.APIView):
    renderer_classes = [CSVRenderer]

    def get_renderer_context(self):
        context = super().get_renderer_context()
        context['header'] = (
            self.request.GET['fields'].split(',')
            if 'fields' in self.request.GET else None)
        return context

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = acc_serializer.UserListingSerializer(instance=users, many=True)
        return response.Response(serializer.data)