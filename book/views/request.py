from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from book.models import Request, Book
from book.serializers import RequestSerializer
from rest_framework.exceptions import PermissionDenied

class RequestCreateView(APIView):
    #autentificirebuli momxmarebeli gvinda da requestis gamgzavni avtomaturad is unda gavxadot
    #POST request, serialize data 
    #return response da status kodi 
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(requester=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RequestListView(APIView):
    # autentifikacia aucilebelia radgan konkretulad Tavisi requestebi unda naxos
    #GET request gvinda
    #egaa ra principshi
    permission_classes = [IsAuthenticated]

    def get(self, request):
        requests = Request.objects.filter(owner = request.user)
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class RequestDecisionView(APIView):
    # aqac avtentificirebul users unda hqondes wvdoma
    # put requesti radgan modificirebaa
    # wignis mflobeli unda iyos sxvas rom ar hqondes modifikaciis sashualeba anu owner == User

    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            request_obj = Request.objects.get(pk=pk)
        except Request.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # tu arsebobs gavagrZeloT 

        if request_obj.book.owner == request.user:
            serializer = RequestSerializer(request_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else: 
            raise PermissionDenied("You haveno Permissin here!")

