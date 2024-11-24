class ColorsMapper:
    colors = {
        "red": '#be185d',
        "green": '#059669',
        "blue": '#1b2779',
    }

    @staticmethod
    def map(color: str) -> str:
        return ColorsMapper.colors.get(color, color)
