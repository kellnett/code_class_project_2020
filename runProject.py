import fun


fun.Initialize()

fun.ShowInstructions()


trials = fun.GenerateTrialSequence()
fun.RandomizeTrialSequence(trials)


'''
testTrials=[[-1,3],[120,12],[-1,6]]
'''

fun.RunTask(trials)
fun.TerminateTask()



