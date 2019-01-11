{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf100
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fswiss\fcharset0 Helvetica-Bold;\f2\froman\fcharset0 Times-Bold;
\f3\froman\fcharset0 Times-Roman;\f4\fnil\fcharset0 Tahoma;\f5\fnil\fcharset0 Tahoma-Bold;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;\red245\green245\blue245;
}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c96863\c96863\c96863;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh18000\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\qc\partightenfactor0

\f0\fs24 \cf0 \ul \ulc0 DOCUMENTATION FOR 
\f1\b PGN
\f0\b0  FORMAT (.pgn)\
\
\pard\pardeftab720\sl380\partightenfactor0

\f2\b\fs32 \cf2 \cb3 \expnd0\expndtw0\kerning0
PGN, the Portable Game Notation formatting.
\f3\b0 \ulnone \
\
This standard format makes it possible to record some of the Chess games\'92s in the text format, that is to say that only the hits are recorded and it is not possible to add variations, comments ... This format is universal and is recognised by all chess software.\
\
This is in fact a simple text file or is stored all the hits of one or more Chess games, as well as additional but optional information between [ ] (names of players, colours, location of game, date, etc )\
A base of parts in the NGP format is indeed a single file, but often large if the base contains millions of parts.\
\
A PGN file (Portable Game Notation) is therefore nothing more and nothing less than a text file ( .txt) that everyone can create/open with a text editor (Windows Note Block for example). To obtain an PGN file, the extension will have to be renamed from a .txt into a .pgn .\
\

\f2\b A PGN file consists of 3 parts:\

\f3\b0 \

\f2\b The header
\f3\b0  (made of tags) =>  it is advisable to have the less number of empty tags ([..]).\

\f2\b The algebraic notation part\
Terminal
\f3\b0  (indicating the outcome of the part)
\f4 \
\

\f5\b \ul More details :
\f4\b0 \ulnone \
\
\pard\pardeftab720\sl340\partightenfactor0

\f5\b\fs28 \cf2 Header (tags)\cb1 \
\pard\pardeftab720\sl340\partightenfactor0

\f4\b0 \cf2 \
\pard\pardeftab720\sl340\partightenfactor0
\cf2 \cb3 A tag is written in syntax: [name_of_tag "value_of_tag"]\cb1 \
\
\pard\pardeftab720\sl340\partightenfactor0

\f5\b \cf2 \cb3 -The 7 basic MANDATORY tags:\
\pard\pardeftab720\sl340\partightenfactor0

\f4\b0 \cf2 \cb1 \
\pard\pardeftab720\sl340\partightenfactor0
\cf2 \cb3 [Event ""] => describes the event, the specificity of the part...\cb1 \
\pard\pardeftab720\sl340\partightenfactor0
\cf2 \cb4 [Site ""] => describes the location.\cb1 \
\pard\pardeftab720\sl340\partightenfactor0
\cf2 \cb3 [Date ""] => date of the event in YYYY.MM.DD format (year, month, day)\cb1 \
\cb3 [Round ""] => indicates the number of turn of the game\cb1 \
\pard\pardeftab720\sl340\partightenfactor0
\cf2 \cb4 [White ""]=> name of the player with whites pieces\cb1 \
\pard\pardeftab720\sl340\partightenfactor0
\cf2 \cb3 [Black ""] =>\cf2 \cb4 name of the player\cf2 \cb3  with black pieces\cb1 \
\pard\pardeftab720\sl340\partightenfactor0
\cf2 \cb4 [result ""] => result of part: 1-0, 0-1, 1/2-1/2 or * in progress, unknown\cb1 \
\
\
\pard\pardeftab720\sl340\partightenfactor0

\f5\b \cf2 The algebraic notation path\
\pard\pardeftab720\sl340\partightenfactor0

\f4\b0 \cf2 \
GENERAL:\
\
-The shots of the game are described with the short algebraic notation in English\
-Before the whites hit, it\'92s always the number of the shot, followed by a point and space.\
\
EX: E4 E5 2. Nf3 Nc6 3. Bb5 A6\
}