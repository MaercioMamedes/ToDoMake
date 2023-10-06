from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from core.serializer import NoteSerializerHard
import requests


class NotePostView(GenericAPIView):
    serializer_class = NoteSerializerHard
    http_method_names = ['post']

    def post(self, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save(comit=False)

            """MUDAR PARA URL DO KAFKA"""
            response = requests.post('http://127.0.0.1:8001/', json=serializer.data)

            if response.status_code == 200:
                return Response(serializer.data)
            else:
                return Response("Deu ruim")
