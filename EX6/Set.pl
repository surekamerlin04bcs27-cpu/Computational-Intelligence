% 1. Union: Elements in either list (removes duplicates)
union([], L, L).
union([H|T], L, [H|Res]) :-
    \+ member(H, L),
    union(T, L, Res).
union([H|T], L, Res) :-
    member(H, L),
    union(T, L, Res).
% 2. Intersection: Elements in both lists
intersection([], _, []).
intersection([H|T], L, [H|Res]) :-
    member(H, L),
    intersection(T, L, Res).
intersection([H|T], L, Res) :-
    \+ member(H, L),
    intersection(T, L, Res).
% 3. Subset: Every element of the first list is in the second
subset([], _).
subset([H|T], L) :-
    member(H, L),
    subset(T, L).
% 4. Cardinality: Number of unique elements
cardinality([], 0).
cardinality([H|T], Count) :-
    member(H, T),
    cardinality(T, Count).
cardinality([H|T], Count) :-
    \+ member(H, T),
    cardinality(T, Rest),
    Count is Rest + 1.
% 5. Equivalent: Both sets are subsets of each other
equivalent(L1, L2) :-
    subset(L1, L2),
    subset(L2, L1).
% 6. Difference (A - B): Elements in A but not in B
difference([], _, []).
difference([H|T], L, [H|Res]) :-
    \+ member(H, L),
    difference(T, L, Res).
difference([H|T], L, Res) :-
    member(H, L),
    difference(T, L, Res).
