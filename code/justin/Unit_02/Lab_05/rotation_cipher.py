class RotationCipher:
    allowed_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    allowed_characters_size = len(allowed_characters)
    rotation = 13


    @classmethod
    def encrypt(cls, text):
        result = ''
        for character in text.lower():
            if character.isalpha():
                index = ord(character) - 97
                result += cls.allowed_characters[(index + cls.rotation) % cls.allowed_characters_size]
            else:
                result += character
        return result