from pprint import pprint
import time

def stairClimbing( totalStepsInt, availableActionList ):

	# list to store all combination of action possible for futher process
	listOfCombinationOfActionList = list()

	# storage for the final combination of action
	finalCombinationOfActionList = list()

	# loop through each available action
	for action in availableActionList:

		# this action is possible
		if action < totalStepsInt:

			# construct storage for this action combination
			combinationOfActionList = [ action ]

			# store this action combination to all possible combination of action
			listOfCombinationOfActionList.append( combinationOfActionList )
	
	# loop until no combination to try
	while listOfCombinationOfActionList:

		# get the first combination of action
		combinationOfActionList = listOfCombinationOfActionList.pop(0)

		# this combination of action can reach the top of stair
		if sum( combinationOfActionList ) == totalStepsInt:

			# store it to final result storage
			finalCombinationOfActionList.append( combinationOfActionList )

			# check the next combination of action
			continue

		# loop through each available action
		for action in availableActionList:

			# this action is possible to add to combination
			if sum( combinationOfActionList ) + action <= totalStepsInt:

				# copy this combination of action to create the new
				# combination of action
				newCombinationOfActionList = combinationOfActionList.copy()

				# add action to the combination
				newCombinationOfActionList.append( action )

				# store the new combination of action for further process
				listOfCombinationOfActionList.append( newCombinationOfActionList )
	
	# return the final result
	return finalCombinationOfActionList

if __name__ == '__main__':

	totalStairStepsInt = 30
	startTimestamp = time.time()
	pprint(stairClimbing( totalStairStepsInt, [ 1, 2 ] ) )
	print( f'Take a total of { time.time() - startTimestamp } to calculate all possible\
		combination of action to climb { totalStairStepsInt } steps stair' )
