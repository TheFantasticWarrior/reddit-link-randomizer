import random

# Directly run the code or replace the code inside [] what you want
# For example
# text=["Not a rickroll"]
# links=["link1","link2","link3"]
text=[input("Text:")]
links=input("Links separated by spaces:").split()

Out=""
for i in range(len(text[0])):
    mtext="[{}]({})".format(text[0][i],random.choice(links))
    Out=Out+mtext
print()
print(Out)

"""
useful links

rickroll
https://youtu.be/dQw4w9WgXcQ https://youtu.be/X-cfWM0BC_4 https://youtu.be/6Mc-Thl1kTQ https://youtu.be/doEqUhFiQS4
https://youtu.be/cSAp9sBzPbc https://youtu.be/wpV-gGA4PSk https://youtu.be/42OleX0HR4E https://youtu.be/X-cfWM0BC_4
https://youtu.be/H01BwSD9eyQ https://youtu.be/SQoA_wjmE9w https://youtu.be/Gc2u6AFImn8 https://youtu.be/FpFztrJbksg
https://youtu.be/cvh0nX08nRw https://www.pornhub.com/view_video.php?viewkey=ph55b2ec08ad5b1
original, forgot lyrics, ytp, give up
c, wrong notes, complicated time travel?, hentai
megalovania, darude sandstorm, shooting star, Astronomia
never start, pornhub

every time he say never do
https://youtu.be/8VFzHYtOARw https://youtu.be/ZXpThNX9IRc https://youtu.be/BCa6gS3uybU https://youtu.be/Oo0twK2ZbLU
bass boost, fast, slow, note change

https://youtu.be/watch?v=MTW4sIL9Dpw https://www.reddit.com/r/YouFellForItFool/comments/cjlngm/you_fell_for_it_fool https://youtu.be/sAn7baRbhx4
thunder cross split attack, again but reddit, spanish inquisition
"""
