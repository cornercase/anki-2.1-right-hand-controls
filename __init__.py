# Eamon Doyle
# Initial Commit - May 6 2019

from anki.hooks import wrap
from aqt.reviewer import Reviewer

def newShortcutKeys(self, _old):
    return _old(self) + [
        ("j", lambda: self._answerCard(1)),
        ("k", lambda: self._answerCard(2)),
        ("l", lambda: self._answerCard(3)),
        (";", lambda: self._answerCard(4)),
    ]

def newAnswerCard(self, ease, _old):
    if self.state == "question":
        self._showAnswer()
    else: 
        _old(self, min(self.mw.col.sched.answerButtons(self.card), ease))

Reviewer._shortcutKeys = wrap(Reviewer._shortcutKeys, newShortcutKeys, "around")
Reviewer._answerCard = wrap(Reviewer._answerCard, newAnswerCard, "around")
