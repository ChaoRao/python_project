# -*- coding: utf-8 -*-
"""一个简单的 Python 示例 demo：猜数字游戏"""

import random


def generate_secret(low: int = 1, high: int = 100) -> int:
    """生成一个随机数作为答案"""
    return random.randint(low, high)


def guess_number(secret: int, max_attempts: int = 7) -> bool:
    """让玩家猜数字，返回是否猜中"""
    print(f"我想了一个 1 到 100 之间的数字，你有 {max_attempts} 次机会！")
    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"第 {attempt} 次猜测，请输入数字: "))
        except ValueError:
            print("输入无效，请输入一个整数。")
            continue

        if guess < secret:
            print("太小了 ⬇️")
        elif guess > secret:
            print("太大了 ⬆️")
        else:
            print(f"🎉 恭喜你，猜对了！答案就是 {secret}")
            return True

    print(f"😢 机会用完了，正确答案是 {secret}")
    return False
def play_again() -> bool:
    """询问玩家是否想再玩一次"""
    choice = input("想不想再玩一次？(y/n): ").lower()
    return choice == 'y' or choice == 'yes'

def main():
    secret = generate_secret()
    guess_number(secret)


if __name__ == "__main__":
    main()
