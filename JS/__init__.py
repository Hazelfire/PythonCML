from jispy import Runtime
rt = Runtime()

#Add Standard Library
rt.runG("JS/stdlib.l.js")

#Add Select Natives
rt.addNatives({'input': lambda prompt: raw_input(prompt)});

#Default Run Function (Accepts FileName)
def run(x):
    x += ".l.js"
    rt.runG(x)

runG = run

#Foreign Run Function (Accepts FileName)
def runForeign(x):
    x += ".l.js"
    rt.runX(x)

runF = runForeign
runX = runF

#Execute String Function (Accepts String)
def runString(x):
    rt.runX(x)

runS = runString

