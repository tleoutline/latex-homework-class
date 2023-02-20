import inquirer
import pyperclip


def format_table():
    matrix_delim = {'Brackets': 'bmatrix*',
                    'Braces': 'Bmatrix*',
                    'Parentheses': 'pmatrix*',
                    'Plain': 'matrix*',
                    'Pipes': 'vmatrix*',
                    'Double pipes': 'Vmatrix*'}

    alignments = {'Left': 'l', 'Centre': 'c', 'Right': 'r'}

    delim_qurestion = [
        inquirer.List('matrix_delim',
                      message="What kind of matrix?",
                      choices=['Brackets', 'Braces', 'Parentheses', 'Plain', 'Pipes', 'Double pipes'])
    ]
    alignment_question = [inquirer.List('alignment',
                                        message='Choose alignment.',
                                        choices=['Right', 'Centre', 'Left'])]

    delim = matrix_delim[inquirer.prompt(delim_qurestion)['matrix_delim']]
    alignment = alignments[inquirer.prompt(alignment_question)['alignment']]

    Matrix = []
    row = input(
        "Enter eace element separated by a space.\n").split(' ')
    while row != ['']:
        Matrix.append(row)
        row = input().split(' ')

    out = f"\\begin{{{delim}}}[{alignment}]\n"
    for i in range(len(Matrix)):
        out += "\t"
        out += " & ".join(Matrix[i])
        if i != len(Matrix) - 1:
            out += "\\\\"
        out += "\n"
    out += f"\\end{{{delim}}}"

    print(out + "\n\n")
    pyperclip.copy(out)
    print("The text is already copied to clipboard.")


def format(format_type):
    if format_type == 'Matrix':
        format_table()

    else:
        print("Feature not available yet.")
        return


def main():
    format_question = [
        inquirer.List('format_type',
                      message="What would you like to format?",
                      choices=['Matrix', 'Table'])
    ]
    answers = inquirer.prompt(format_question)
    format(answers['format_type'])


if __name__ == '__main__':
    main()
