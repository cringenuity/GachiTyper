from SubstitutionList import SubstitutionList
from Substitution import Substitution

class ConflictSearcher:
    def search_conflicts(self, subs: SubstitutionList) -> \
        list[tuple[Substitution, Substitution]]:
        sorted_subs = sorted(
            subs.substitutions,
            key=lambda x: len(x.source))

        conflicts = []

        for i in range(len(sorted_subs)):
            for j in range(i + 1, len(sorted_subs)):
                if sorted_subs[i].source in sorted_subs[j].source:
                    conflicts.append((sorted_subs[i], sorted_subs[j]))

        return conflicts
