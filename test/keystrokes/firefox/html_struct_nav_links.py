#!/usr/bin/python

"""Test of structural navigation amongst links."""

from macaroon.playback import *
import utils

sequence = MacroSequence()

sequence.append(KeyComboAction("<Control>Home"))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("u"))
sequence.append(utils.AssertPresentationAction(
    "1. u to anchors.html link",
    ["BRAILLE LINE:  '•anchors.html'",
     "     VISIBLE:  '•anchors.html', cursor=2",
     "BRAILLE LINE:  '•anchors.html'",
     "     VISIBLE:  '•anchors.html', cursor=2",
     "SPEECH OUTPUT: 'anchors.html'",
     "SPEECH OUTPUT: 'link' voice=hyperlink"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("u"))
sequence.append(utils.AssertPresentationAction(
    "2. u to blockquotes.html link",
    ["BRAILLE LINE:  '•blockquotes.html'",
     "     VISIBLE:  '•blockquotes.html', cursor=2",
     "BRAILLE LINE:  '•blockquotes.html'",
     "     VISIBLE:  '•blockquotes.html', cursor=2",
     "SPEECH OUTPUT: 'blockquotes.html'",
     "SPEECH OUTPUT: 'link' voice=hyperlink"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("<Shift>u"))
sequence.append(utils.AssertPresentationAction(
    "3. shift + u to anchors.html link",
    ["BRAILLE LINE:  '•anchors.html'",
     "     VISIBLE:  '•anchors.html', cursor=2",
     "BRAILLE LINE:  '•anchors.html'",
     "     VISIBLE:  '•anchors.html', cursor=2",
     "SPEECH OUTPUT: 'anchors.html'",
     "SPEECH OUTPUT: 'link' voice=hyperlink"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("<Shift>u"))
sequence.append(utils.AssertPresentationAction(
    "4. shift + u wrapping to bottom",
    ["BRAILLE LINE:  'Wrapping to bottom.'",
     "     VISIBLE:  'Wrapping to bottom.', cursor=0",
     "BRAILLE LINE:  '•textattributes.html'",
     "     VISIBLE:  '•textattributes.html', cursor=2",
     "BRAILLE LINE:  '•textattributes.html'",
     "     VISIBLE:  '•textattributes.html', cursor=2",
     "SPEECH OUTPUT: 'Wrapping to bottom.' voice=system",
     "SPEECH OUTPUT: 'textattributes.html'",
     "SPEECH OUTPUT: 'link' voice=hyperlink"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("<Shift>u"))
sequence.append(utils.AssertPresentationAction(
    "5. shift + u to tables.html",
    ["BRAILLE LINE:  '•tables.html'",
     "     VISIBLE:  '•tables.html', cursor=2",
     "BRAILLE LINE:  '•tables.html'",
     "     VISIBLE:  '•tables.html', cursor=2",
     "SPEECH OUTPUT: 'tables.html'",
     "SPEECH OUTPUT: 'link' voice=hyperlink"]))

sequence.append(KeyComboAction("Return"))
sequence.append(WaitForDocLoad())

sequence.append(KeyComboAction("<Alt>Left"))
sequence.append(WaitForDocLoad())

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("u"))
sequence.append(utils.AssertPresentationAction(
    "6. u to textattributes.html link",
    ["BRAILLE LINE:  '•textattributes.html'",
     "     VISIBLE:  '•textattributes.html', cursor=2",
     "BRAILLE LINE:  '•textattributes.html'",
     "     VISIBLE:  '•textattributes.html', cursor=2",
     "SPEECH OUTPUT: 'textattributes.html'",
     "SPEECH OUTPUT: 'link' voice=hyperlink"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("u"))
sequence.append(utils.AssertPresentationAction(
    "7. u to anchors.html link",
    ["BRAILLE LINE:  'Wrapping to top.'",
     "     VISIBLE:  'Wrapping to top.', cursor=0",
     "BRAILLE LINE:  '•anchors.html'",
     "     VISIBLE:  '•anchors.html', cursor=2",
     "BRAILLE LINE:  '•anchors.html'",
     "     VISIBLE:  '•anchors.html', cursor=2",
     "SPEECH OUTPUT: 'Wrapping to top.' voice=system",
     "SPEECH OUTPUT: 'anchors.html'",
     "SPEECH OUTPUT: 'link' voice=hyperlink"]))

sequence.append(KeyComboAction("Return"))
sequence.append(WaitForDocLoad())

sequence.append(KeyComboAction("<Alt>Left"))
sequence.append(WaitForDocLoad())

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("v"))
sequence.append(utils.AssertPresentationAction(
    "8. v to tables.html link",
    ["BRAILLE LINE:  '•tables.html'",
     "     VISIBLE:  '•tables.html', cursor=2",
     "BRAILLE LINE:  '•tables.html'",
     "     VISIBLE:  '•tables.html', cursor=2",
     "SPEECH OUTPUT: 'tables.html'",
     "SPEECH OUTPUT: 'link' voice=hyperlink"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("v"))
sequence.append(utils.AssertPresentationAction(
    "9. v to blockquotes.html link",
    ["BRAILLE LINE:  'Wrapping to top.'",
     "     VISIBLE:  'Wrapping to top.', cursor=0",
     "BRAILLE LINE:  '•anchors.html'",
     "     VISIBLE:  '•anchors.html', cursor=2",
     "BRAILLE LINE:  '•anchors.html'",
     "     VISIBLE:  '•anchors.html', cursor=2",
     "SPEECH OUTPUT: 'Wrapping to top.' voice=system",
     "SPEECH OUTPUT: 'anchors.html'",
     "SPEECH OUTPUT: 'link' voice=hyperlink"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("<Shift>v"))
sequence.append(utils.AssertPresentationAction(
    "10. shift + v to tables.html link",
    ["BRAILLE LINE:  'Wrapping to bottom.'",
     "     VISIBLE:  'Wrapping to bottom.', cursor=0",
     "BRAILLE LINE:  '•tables.html'",
     "     VISIBLE:  '•tables.html', cursor=2",
     "BRAILLE LINE:  '•tables.html'",
     "     VISIBLE:  '•tables.html', cursor=2",
     "SPEECH OUTPUT: 'Wrapping to bottom.' voice=system",
     "SPEECH OUTPUT: 'tables.html'",
     "SPEECH OUTPUT: 'link' voice=hyperlink"]))

sequence.append(utils.AssertionSummaryAction())
sequence.start()
