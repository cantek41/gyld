class ArrayHelper():
    @staticmethod
    def get_key(value,array):
        for key, val in array.items():
            if value == val:
                return key