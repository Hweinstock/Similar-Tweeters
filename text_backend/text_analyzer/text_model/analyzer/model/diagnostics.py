
def generate_diagnostics(actual_results, predicted_results):

    combined_results = zip(actual_results, predicted_results)

    total_different_authors = 0.0
    correct_different_authors = 0.0

    total_same_authors = 0.0
    correct_same_authors = 0.0

    total_same_author_guesses = 0.0
    correct_same_author_guesses = 0.0

    total = 0.0
    correct = 0.0

    for actual, predicted in combined_results:
        total += 1.0
        if predicted == True:
            total_same_author_guesses += 1.0
            if actual == True:
                correct_same_author_guesses += 1.0

        if actual == False:
            total_different_authors += 1.0
            if predicted == False:
                correct_different_authors += 1.0
                correct += 1.0

        else:
            total_same_authors += 1.0
            if predicted == True:
                correct_same_authors += 1.0
                correct += 1.0

    if total_different_authors != 0.0:
        print("% of different authors identified:", correct_different_authors/total_different_authors * 100.0)

    if total_same_authors != 0.0:
        print("% of same authors identified:", correct_same_authors/total_same_authors * 100.0)

    if total_same_author_guesses != 0.0:
        print("% correct when guessing same authors:", correct_same_author_guesses / total_same_author_guesses * 100.0)

    print("Overall % Correct:", correct/total * 100.0)