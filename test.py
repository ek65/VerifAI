import verifai
import scenic
from verifai.samplers.scenic_sampler import *

scenic_file = '/home/ek65/Desktop/VerifAI/2vs2_with_scenic_high_pass_forward.scenic'
scenario = scenic.scenarioFromFile(scenic_file)
# space, _ = spaceForScenario(scenario)

sampler = ScenicSampler(scenario)
# scene = scenario.generate(maxIterations=2000, feedback=None)
output = sampler.nextSample()
print(output)