class Smart_samurai:
    # クラス変数
    total_samurais = 0
    default_python_level = 3
    community_name = '佐賀スマートサムライ'
    # コンストラクタ
    def __init__(self, name: str, period: int, python_level: int):
        self.name = name
        self.period = period
        self.python_level = python_level  # propertyで管理
        #クラスメソッドの際追加
        Smart_samurai.total_samurais += 1

    # デストラクタ
    def __del__(self):
        Smart_samurai.total_samurais -= 1
        print(f"{self.name} が削除されました。現在の総人数: {Smart_samurai.total_samurais}")

    # 自己紹介メソッド (インスタンスメソッド）
    def introduce(self):
        return f"{self.community_name}の{self.name}です。SAGA_SMART_SAMURAI{self.period}期生です。Pythonレベルは{self.python_level}です。"
    # レベルアップメソッド
    def python_level_up(self, increment: int):
        self.python_level += increment
    # クラスメソッド: デフォルト値でインスタンスを作成　クラスメソッド:クラス全体に関する操作や情報の提供を行う
    @classmethod
    def create_with_default_level(cls, name: str, period: int):
        return cls(name, period, cls.default_python_level)
    # クラスメソッド: 現在の総人数を取得
    @classmethod
    def get_total_samurais(cls):
        return f"SAGA_SMART_SAMURAIの総人数は{cls.total_samurais}人です。"


#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ここまで前回の内容。~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @classmethod
    def fun_of_community_by_classmethod(cls) -> str:
        """
        クラスメソッドでコミュニティを称賛する
        """
        pass

    @staticmethod
    def fun_of_community_by_staticmethod() -> str:
        """
        スタティックメソッドでコミュニティを称賛する
        """
        pass

    # 特殊メソッド: 演算子のオーバーロード
    # インスタンスを演算子で結んだ時の挙動を指定
    def __add__(self, other: 'Smart_samurai') -> str:
        """
        2人のPythonレベルを加算する
        例　print(samurai1 + samurai2)
        "太朗（samurai1）と二郎（samurai2）が融合するとpythonレベルは15になるよ。"
        """
        pass

    def __sub__(self, other: 'Smart_samurai') -> str:
        """
        2人のPythonレベルの差を計算する
        """
        pass

    def __mul__(self, other: 'Smart_samurai') -> str:
        """
        2人のPythonレベルを掛け算する
        """
        pass

    def __truediv__(self, other: 'Smart_samurai') -> str:
        """
        2人のPythonレベルを割り算する
        """
        pass

    def __eq__(self, other: 'Smart_samurai') -> str:
        """
        2人のPythonレベルを比較する
        """
        pass

    # property: python_level の取得に制限を設ける
    @property
    def python_level(self) -> int:
        """
        Pythonレベルを取得する
        """
        pass

    # setter: python_level の設定（1未満にはならないようにする）
    @python_level.setter
    def python_level(self, value: int) -> None:
        """
        Pythonレベルを設定する（最低値を3に制限）
        """
        pass
