
def generate_diagnostics(actual_results, predicted_results):

    combined_results = zip(actual_results, predicted_results)

    total_different_authors = 0
    correct_different_authors = 0

    total_same_authors = 0
    correct_same_authors = 0

    total_same_author_guesses = 0
    correct_same_author_guesses = 0

    total = 0
    correct = 0

    for actual, predicted in combined_results:
        total += 1
        if predicted == True:
            total_same_author_guesses += 1
            if actual == True:
                correct_same_author_guesses += 1

        if actual == False:
            total_different_authors += 1
            if predicted == False:
                correct_different_authors += 1
                correct += 1

        else:
            total_same_authors += 1
            if predicted == True:
                correct_same_authors += 1
                correct += 1

    print("% of different authors identified:", correct_different_authors/total_different_authors * 100)

    print("% of same authors identified:", correct_same_authors/total_same_authors * 100)

    print("% correct when guessing same authors:", correct_same_author_guesses / total_same_author_guesses * 100)

    print("Overall % Correct:", correct/total * 100)