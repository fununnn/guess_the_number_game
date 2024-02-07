import subprocess
import sys

"""
さて、標準的なストリームを扱ったので、今度はこの知識を使ってプログラムを作ってみましょう。
この課題では、ユーザーに 2 つの数字、最小数（n）と最大数（m）を入力してもらうことになります。
最小値が最大値以下であることを確認することが重要です。
ユーザーは、この 2 つの数字を入力すると、プログラムが n から m の範囲内で乱数を生成します。
その後、ユーザーは乱数を正しく推測するまで、ゲームループの中で繰り返し数字を入力することに
なります。与えられた範囲内の乱数を生成するには、random モジュールと randint 関数を
使用してください。ゲームをより難しくするために、ユーザーが数字を推測するための試行回数を
制限することができます。この場合、for 文で最大 n 回の試行を行うか、while 文でユーザーが
数字を正しく当てるまで繰り返し入力する方法があります。
"""



