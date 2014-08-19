#!/usr/bin/python

"""Test of sayAll."""

from macaroon.playback import *
import utils

sequence = MacroSequence()

sequence.append(KeyComboAction("<Shift>Tab"))
sequence.append(KeyComboAction("<Shift>Tab"))
sequence.append(KeyComboAction("<Control>Home"))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_Add"))
sequence.append(utils.AssertPresentationAction(
    "KP_Add to do a SayAll",
    ["SPEECH OUTPUT: 'Home'",
     "SPEECH OUTPUT: 'Bugzilla'",
     "SPEECH OUTPUT: 'New bug'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' · '",
     "SPEECH OUTPUT: 'Browse'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' · '",
     "SPEECH OUTPUT: 'Search'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' · '",
     "SPEECH OUTPUT: 'Reports'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' · '",
     "SPEECH OUTPUT: 'Account'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' · '",
     "SPEECH OUTPUT: 'Admin'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' · '",
     "SPEECH OUTPUT: 'Help'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Logged In joanmarie.diggs@gmail.com | '",
     "SPEECH OUTPUT: 'Log Out'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' '",
     "SPEECH OUTPUT: 'Short Bug Search Form '",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Complicated Bug Search Form'",
     "SPEECH OUTPUT: ' '",
     "SPEECH OUTPUT: 'Give me some help'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' (reloads page.)'",
     "SPEECH OUTPUT: 'Summary:'",
     "SPEECH OUTPUT: 'row header'",
     "SPEECH OUTPUT: 'Summary: contains all of the words/strings combo box'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'Search push button'",
     "SPEECH OUTPUT: 'Classification:'",
     "SPEECH OUTPUT: 'column header'",
     "SPEECH OUTPUT: 'Classification: Admin multi-select List with 8 items'",
     "SPEECH OUTPUT: 'Product:'",
     "SPEECH OUTPUT: 'column header'",
     "SPEECH OUTPUT: 'Product: accerciser multi-select List with 379 items'",
     "SPEECH OUTPUT: 'Component'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ': '",
     "SPEECH OUTPUT: 'column header'",
     "SPEECH OUTPUT: 'Component: abiscan multi-select List with 1248 items'",
     "SPEECH OUTPUT: 'Version:'",
     "SPEECH OUTPUT: 'column header'",
     "SPEECH OUTPUT: 'Version: 0.0.1 multi-select List with 857 items'",
     "SPEECH OUTPUT: 'Target Milestone:'",
     "SPEECH OUTPUT: 'column header'",
     "SPEECH OUTPUT: 'Target Milestone: --- multi-select List with 555 items'",
     "SPEECH OUTPUT: 'A Comment:'",
     "SPEECH OUTPUT: 'row header'",
     "SPEECH OUTPUT: 'contains the string combo box'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'blank'",
     "SPEECH OUTPUT: 'Whiteboard:'",
     "SPEECH OUTPUT: 'row header'",
     "SPEECH OUTPUT: 'contains all of the words/strings combo box'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'blank'",
     "SPEECH OUTPUT: 'Keywords'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ': '",
     "SPEECH OUTPUT: 'row header'",
     "SPEECH OUTPUT: 'contains all of the keywords combo box'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'separator'",
     "SPEECH OUTPUT: 'Status:'",
     "SPEECH OUTPUT: 'column header'",
     "SPEECH OUTPUT: 'Status:'",
     "SPEECH OUTPUT: 'UNCONFIRMED NEW ASSIGNED REOPENED NEEDINFO'",
     "SPEECH OUTPUT: 'multi-select List with 8 items'",
     "SPEECH OUTPUT: 'Resolution: '",
     "SPEECH OUTPUT: 'column header'",
     "SPEECH OUTPUT: 'Resolution:'",
     "SPEECH OUTPUT: 'FIXED'",
     "SPEECH OUTPUT: 'multi-select List with 12 items'",
     "SPEECH OUTPUT: 'Severity:'",
     "SPEECH OUTPUT: 'column header'",
     "SPEECH OUTPUT: 'Severity: blocker multi-select List with 7 items'",
     "SPEECH OUTPUT: 'Priority:'",
     "SPEECH OUTPUT: 'column header'",
     "SPEECH OUTPUT: 'Priority: Immediate multi-select List with 5 items'",
     "SPEECH OUTPUT: 'OS:'",
     "SPEECH OUTPUT: 'column header'",
     "SPEECH OUTPUT: 'OS: All multi-select List with 21 items'",
     "SPEECH OUTPUT: 'Email and Numbering'",
     "SPEECH OUTPUT: 'Any one of:'",
     "SPEECH OUTPUT: 'check box checked'",
     "SPEECH OUTPUT: ' the bug assignee'",
     "SPEECH OUTPUT: 'check box not checked'",
     "SPEECH OUTPUT: ' the reporter'",
     "SPEECH OUTPUT: 'check box not checked'",
     "SPEECH OUTPUT: ' the QA contact'",
     "SPEECH OUTPUT: 'check box not checked'",
     "SPEECH OUTPUT: ' a CC list member'",
     "SPEECH OUTPUT: 'check box not checked'",
     "SPEECH OUTPUT: ' a commenter'",
     "SPEECH OUTPUT: 'contains combo box'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'Any one of:'",
     "SPEECH OUTPUT: 'check box checked'",
     "SPEECH OUTPUT: ' the bug assignee'",
     "SPEECH OUTPUT: 'check box checked'",
     "SPEECH OUTPUT: ' the reporter'",
     "SPEECH OUTPUT: 'check box checked'",
     "SPEECH OUTPUT: ' the QA contact'",
     "SPEECH OUTPUT: 'check box checked'",
     "SPEECH OUTPUT: ' a CC list member'",
     "SPEECH OUTPUT: 'check box not checked'",
     "SPEECH OUTPUT: ' a commenter'",
     "SPEECH OUTPUT: 'contains combo box'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'separator'",
     "SPEECH OUTPUT: 'Only include combo box'",
     "SPEECH OUTPUT: 'bugs numbered:'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'blank'",
     "SPEECH OUTPUT: '(comma-separated list)'",
     "SPEECH OUTPUT: 'Bug Changes'",
     "SPEECH OUTPUT: 'Only bugs changed between:'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: ' and entry Now ",
     "(YYYY-MM-DD or relative dates)'",
     "SPEECH OUTPUT: 'where one or more of the following changed:'",
     "SPEECH OUTPUT: 'where one or more of the following changed: [Bug creation] multi-select List with 26 items'",
     "SPEECH OUTPUT: 'and the new value was:'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'GNOME version:'",
     "SPEECH OUTPUT: 'column header'",
     "SPEECH OUTPUT: 'GNOME version: Unspecified multi-select List with 14 items'",
     "SPEECH OUTPUT: 'GNOME target:'",
     "SPEECH OUTPUT: 'column header'",
     "SPEECH OUTPUT: 'GNOME target: Unspecified multi-select List with 12 items'",
     "SPEECH OUTPUT: 'Sort results by: Reuse same sort as last time combo box'",
     "SPEECH OUTPUT: 'Search push button'",
     "SPEECH OUTPUT: '    check box not checked  and remember these as my default search options'",
     "SPEECH OUTPUT: 'separator'",
     "SPEECH OUTPUT: 'Advanced Searching Using Boolean Charts:'",
     "SPEECH OUTPUT: 'check box not checked'",
     "SPEECH OUTPUT: ' Not (negate this whole chart)'",
     "SPEECH OUTPUT: '--- combo box'",
     "SPEECH OUTPUT: '--- combo box entry'",
     "SPEECH OUTPUT: 'Or push button'",
     "SPEECH OUTPUT: 'And push button'",
     "SPEECH OUTPUT: '       Add another boolean chart push button       '",
     "SPEECH OUTPUT: 'separator'",
     "SPEECH OUTPUT: 'Saved Searches: '",
     "SPEECH OUTPUT: 'My Bugs and Patches'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' | '",
     "SPEECH OUTPUT: 'All Orca'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' | '",
     "SPEECH OUTPUT: 'Firefox'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' | '",
     "SPEECH OUTPUT: 'open orca'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' | '",
     "SPEECH OUTPUT: 'Open RFEs'",
     "SPEECH OUTPUT: 'link'"]))

sequence.append(utils.AssertionSummaryAction())
sequence.start()
