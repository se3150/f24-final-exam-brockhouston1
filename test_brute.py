import pytest
from brute import Brute
import hashlib

def describe_Brute():

    @pytest.fixture
    def cracker():
        return Brute("TDD")

    def describe_bruteOnce():
        
        def it_returns_true_when_correct_password_attempted(cracker):
            assert cracker.bruteOnce("TDD") == True
            
        def it_returns_false_when_incorrect_password_attempted(cracker):
            assert cracker.bruteOnce("wrong") == False
            
        def it_handles_empty_string_attempt(cracker):
            assert cracker.bruteOnce("") == False
            
        def it_is_case_sensitive(cracker):
            assert cracker.bruteOnce("tdd") == False

    def hash():

        # idk maybe they want to use our program
        def it_works_when_given_chinese_characters_lol(cracker):
            assert cracker.hash("软件") == hashlib.sha512(bytes("软件","utf-8")).hexdigest()


    def describe_bruteMany():
        
        def it_returns_time_when_password_found(cracker, mocker):
            mocker.patch.object(
                cracker, 
                'randomGuess',
                side_effect=["wrong", "TDD"]
            )
            result = cracker.bruteMany(limit=2)
            assert result > 0
            
        def it_returns_negative_one_when_password_not_found(cracker, mocker):
            # stub randomGuess method to always return bad guesses
            mocker.patch.object(
                cracker,
                'randomGuess',
                return_value="wrong"
            )
            # shoudlnt guess the password in three randomGuess calls
            assert cracker.bruteMany(limit=3) == -1
            
        def it_respects_attempt_limit(cracker, mocker):
            # mock randomGuess to verify number of calls
            mock_guess = mocker.patch.object(cracker, 'randomGuess')
            mock_guess.return_value = "wrong"
            
            cracker.bruteMany(limit=5)
            assert mock_guess.call_count == 5
            
        def it_stops_when_password_found(cracker, mocker):
            # mock randoGuess to make sure it stops after finding correct pass
            mock_guess = mocker.patch.object(
                cracker,
                'randomGuess',
                side_effect=["wrong", "TDD", "dontcallmeplz_I_should_not_beCalled"]
            )
            
            cracker.bruteMany(limit=3)
            # should stop after finding second side_effect
            assert mock_guess.call_count == 2  
