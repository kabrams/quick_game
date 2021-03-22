import pytest
from . import rock_paper_scissors 

def test_rules():
	assert rock_paper_scissors.rules('Rock','Rock') == "You picked Rock, computer picked Rock - it's tied."
	assert rock_paper_scissors.rules('Rock', 'Paper') == "You picked Rock, computer picked Paper - you lose!"
	assert rock_paper_scissors.rules('Rock', 'Scissors') == "You picked Rock, computer picked Scissors - you win!!"
	assert rock_paper_scissors.rules('Paper','Paper') == "You picked Paper, computer picked Paper - it's tied."
	assert rock_paper_scissors.rules('Paper', 'Scissors') == "You picked Paper, computer picked Scissors - you lose!"
	assert rock_paper_scissors.rules('Paper', 'Rock') == "You picked Paper, computer picked Rock - you win!!"
	assert rock_paper_scissors.rules('Scissors','Scissors') == "You picked Scissors, computer picked Scissors - it's tied."
	assert rock_paper_scissors.rules('Scissors', 'Rock') == "You picked Scissors, computer picked Rock - you lose!"
	assert rock_paper_scissors.rules('Scissors', 'Paper') == "You picked Scissors, computer picked Paper - you win!!"