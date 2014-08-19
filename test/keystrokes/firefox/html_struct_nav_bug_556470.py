#!/usr/bin/python

"""Test of table structural navigation with empty tables."""

from macaroon.playback import *
import utils

sequence = MacroSequence()
sequence.append(KeyComboAction("<Control>Home"))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("t"))
sequence.append(utils.AssertPresentationAction(
    "1. t",
    ["BRAILLE LINE:  'table with 2 rows 3 columns'",
     "     VISIBLE:  'table with 2 rows 3 columns', cursor=0",
     "BRAILLE LINE:  'col 1 col 2 col 3'",
     "     VISIBLE:  'col 1 col 2 col 3', cursor=1",
     "SPEECH OUTPUT: 'table with 2 rows 3 columns' voice=system",
     "SPEECH OUTPUT: 'col 1'",
     "SPEECH OUTPUT: 'column header'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("t"))
sequence.append(utils.AssertPresentationAction(
    "2. t",
    ["BRAILLE LINE:  'table with 2 rows 3 columns'",
     "     VISIBLE:  'table with 2 rows 3 columns', cursor=0",
     "BRAILLE LINE:  '1 2 4'",
     "     VISIBLE:  '1 2 4', cursor=1",
     "SPEECH OUTPUT: 'table with 2 rows 3 columns'",
     "SPEECH OUTPUT: '1'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("t"))
sequence.append(utils.AssertPresentationAction(
    "3. t",
    ["BRAILLE LINE:  'Wrapping to top.'",
     "     VISIBLE:  'Wrapping to top.', cursor=0",
     "BRAILLE LINE:  'table with 2 rows 3 columns'",
     "     VISIBLE:  'table with 2 rows 3 columns', cursor=0",
     "BRAILLE LINE:  'col 1 col 2 col 3'",
     "     VISIBLE:  'col 1 col 2 col 3', cursor=1",
     "SPEECH OUTPUT: 'Wrapping to top.' voice=system",
     "SPEECH OUTPUT: 'table with 2 rows 3 columns' voice=system",
     "SPEECH OUTPUT: 'col 1'",
     "SPEECH OUTPUT: 'column header'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("<Shift>t"))
sequence.append(utils.AssertPresentationAction(
    "4. shift+t", 
    ["BRAILLE LINE:  'Wrapping to bottom.'",
     "     VISIBLE:  'Wrapping to bottom.', cursor=0",
     "BRAILLE LINE:  'table with 2 rows 3 columns'",
     "     VISIBLE:  'table with 2 rows 3 columns', cursor=0",
     "BRAILLE LINE:  '1 2 4'",
     "     VISIBLE:  '1 2 4', cursor=1",
     "SPEECH OUTPUT: 'Wrapping to bottom.'",
     "SPEECH OUTPUT: 'table with 2 rows 3 columns'",
     "SPEECH OUTPUT: '1'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("<Shift>t"))
sequence.append(utils.AssertPresentationAction(
    "5. shift+t", 
    ["BRAILLE LINE:  'table with 2 rows 3 columns'",
     "     VISIBLE:  'table with 2 rows 3 columns', cursor=0",
     "BRAILLE LINE:  'col 1 col 2 col 3'",
     "     VISIBLE:  'col 1 col 2 col 3', cursor=1",
     "SPEECH OUTPUT: 'table with 2 rows 3 columns' voice=system",
     "SPEECH OUTPUT: 'col 1'",
     "SPEECH OUTPUT: 'column header'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("<Shift>t"))
sequence.append(utils.AssertPresentationAction(
    "6. shift+t",
    ["BRAILLE LINE:  'Wrapping to bottom.'",
     "     VISIBLE:  'Wrapping to bottom.', cursor=0",
     "BRAILLE LINE:  'table with 2 rows 3 columns'",
     "     VISIBLE:  'table with 2 rows 3 columns', cursor=0",
     "BRAILLE LINE:  '1 2 4'",
     "     VISIBLE:  '1 2 4', cursor=1",
     "SPEECH OUTPUT: 'Wrapping to bottom.'",
     "SPEECH OUTPUT: 'table with 2 rows 3 columns'",
     "SPEECH OUTPUT: '1'"]))

sequence.append(utils.AssertionSummaryAction())
sequence.start()
