from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ Serializes a name field to test API View"""

    name = serializers.CharField(max_length=10)
