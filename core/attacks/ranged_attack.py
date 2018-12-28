from core.attacks.attack import Attack


class RangedAttack(Attack):
    def __init__(self, attributes=None, size_bonus=0, misc_bonus=0, base_mod=0, attack_attribute='dex'):
        super(RangedAttack, self).__init__(attributes=attributes, size_bonus=size_bonus, misc_bonus=misc_bonus,
                                           base_mod=base_mod, attack_attribute=attack_attribute)
