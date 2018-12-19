# PolyChess By Alpha0

Trello link : https://trello.com/b/2kFbD5MU/notre-projet

Discord server link (for supervision) : https://discord.gg/E3SM5VJ

PolyChess (named polychess as Git repository) is a Chess engine written in Python and modified by Alpha0, a team of students on a course on project management at the engineering school Polytech Annecy-Chambéry.

The aim of this repository is not to provide any complete Chess engine but the best version the team can develop following the client requests. As a consequence, persons interested in this project should check the different forks.

The required features for PolyChess are:

* PolyChess is able to play against a user, or to play against itself (through UCI and Winboard on Windows, or Arena on Mac)
* The games played are stored in PGN format in a directory games, the PGN headers have to be filled
* PolyChess can render the board either in text (on the console) or in SVG (thanks to python-chess, in Jupyter Notebooks)
* PolyChess has an opening book (first as a Polyglot book, then using your own format)
* PolyChess is able to play on Lichess (and eventually FICS)
* PolyChess is modular, it is then easy to isolate a feature and to modify it
* PolyChess has an AI (easy to modify) that could play for the engine
* It is possible to enter a FEN position and obtain an evaluation from PolyChess

## Milestones for the project

Milestone 1:

PolyChess is able to play against user or another engine through UCI, has an opening book and an AI

Milestone 2:
PolyChess plays on Lichess (and FICS)

Milestone 3:

Board representation and legal moves are no longer provided by python-chess but are students' responsibilities

## New techniques/skills/terms to get acquainted with

* Chess (maybe)
* Universal Chess Interface (UCI) (http://wbec-ridderkerk.nl/html/UCIProtocol.html)
* Portable General Notation (PGN)
* Board representation (bitboards, 0x88, 120-square representation, 64-square representation)
* MinMax (Negamax)
* Alpha-Beta pruning
* Chess rules (five fold repetition, seventy-five moves)
* Opening book (Polyglot)
* Forsyth-Edwards Notation (FEN) (https://www.chessprogramming.org/Forsyth-Edwards_Notation)
* Piece-Square table
* Move ordering
* Position evaluation
* Transposition table
* Zobrist key
* Perft

# Alpha0 team :
* Robin COLLIAUX  - Chief
* Rémy MARTIN     - Developer
* Nadia HAMADOU   - Developer
* Beda IGIRANEZA  - Developer

DS


    # Readme for PGN format (BEDA I.)

                DOCUMENTATION FOR PGN FORMAT (.pgn)

                PGN, the Portable Game Notation formatting.

                This standard format makes it possible to record some of the Chess games’s in the text format, that is to say                 that only the hits are recorded and it is not possible to add variations, comments ... This format is                         universal and is recognised by all chess software.

                This is in fact a simple text file or is stored all the hits of one or more Chess games, as well as additional                 but optional information between [ ] (names of players, colours, location of game, date, etc )
                A base of parts in the NGP format is indeed a single file, but often large if the base contains millions of                   parts.

                A PGN file (Portable Game Notation) is therefore nothing more and nothing less than a text file ( .txt) that                   everyone can create/open with a text editor (Windows Note Block for example). To obtain an PGN file, the                       extension will have to be renamed from a .txt into a .pgn .

                A PGN file consists of 3 parts:

                The header (made of tags) =>  it is advisable to have the less number of empty tags ([..]).
                The algebraic notation part
                Terminal (indicating the outcome of the part)

                More details :

                Header (tags)

                A tag is written in syntax: [name_of_tag "value_of_tag"]

                -The 7 basic MANDATORY tags:

                [Event ""] => describes the event, the specificity of the part...
                [Site ""] => describes the location.
                [Date ""] => date of the event in YYYY.MM.DD format (year, month, day)
                [Round ""] => indicates the number of turn of the game
                [White ""]=> name of the player with whites pieces
                [Black ""] =>name of the player with black pieces
                [result ""] => result of part: 1-0, 0-1, 1/2-1/2 or * in progress, unknown


                The algebraic notation path

                GENERAL:

                -The shots of the game are described with the short algebraic notation in English
                -Before the whites hit, it’s always the number of the shot, followed by a point and space.

                EX: E4 E5 2. Nf3 Nc6 3. Bb5 A6
