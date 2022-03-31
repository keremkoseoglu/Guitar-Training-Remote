""" Practice category """
from enum import Enum

class PracticeCategory(Enum):
    """ Practice category """
    UNDEFINED = 0
    RIGHT_HAND = 1
    LEFT_HAND = 2
    THEORY = 3
    DEXTERITY = 4
    PERFORMANCE = 5
    EDUCATION = 6

class PracticeCategoryGroup(Enum):
    """ Practice category group """
    UNDEFINED = 0
    TECHNIQUE = 1
    THEORY = 2
    DEXTERITY = 3
    PERFORMANCE = 4
    EDUCATION = 5

def get_category_group(category: PracticeCategory) -> PracticeCategoryGroup:
    """ Converts category to group """
    if category == PracticeCategory.UNDEFINED:
        return PracticeCategoryGroup.UNDEFINED
    if category in (PracticeCategory.RIGHT_HAND, PracticeCategory.LEFT_HAND):
        return PracticeCategoryGroup.TECHNIQUE
    if category == PracticeCategory.THEORY:
        return PracticeCategoryGroup.THEORY
    if category == PracticeCategory.DEXTERITY:
        return PracticeCategoryGroup.DEXTERITY
    if category == PracticeCategory.PERFORMANCE:
        return PracticeCategoryGroup.PERFORMANCE
    if category == PracticeCategory.EDUCATION:
        return PracticeCategoryGroup.EDUCATION
    raise Exception(f"Undefined category {category.name}")
