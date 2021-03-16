import pytest
from rock_paper_scissors import *

def test_rules():
	assert rules('Rock','Rock') == "You picked Rock, computer picked Rock - it's tied."
	assert rules('Rock', 'Paper') == "You picked Rock, computer picked Paper - you lose!"
	assert rules('Rock', 'Scissors') == "You picked Rock, computer picked Scissors - you win!!"
	assert rules('Paper','Paper') == "You picked Paper, computer picked Paper - it's tied."
	assert rules('Paper', 'Scissors') == "You picked Paper, computer picked Scissors - you lose!"
	assert rules('Paper', 'Rock') == "You picked Paper, computer picked Rock - you win!!"
	assert rules('Scissors','Scissors') == "You picked Scissors, computer picked Scissors - it's tied."
	assert rules('Scissors', 'Rock') == "You picked Scissors, computer picked Rock - you lose!"
	assert rules('Scissors', 'Paper') == "You picked Scissors, computer picked Paper - you win!!"