import adjudicator as adj
import greedy_interface as agent

def main():
	a1, a2 = agent.Agent(), agent.Agent()

	adjudicator = adj.Adjudicator(a1, a2)

	adjudicator.play()




if(__name__ == "__main__"):
	main()
