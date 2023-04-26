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
                source1 = sorted_subs[i].source
                source2 = sorted_subs[j].source

                if source1 in source2 and not source2.endswith(source1):
                    conflicts.append((sorted_subs[i], sorted_subs[j]))

        return conflicts
