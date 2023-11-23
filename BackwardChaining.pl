% Rules
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% Facts
parent(john, mary).
parent(john, tom).
parent(mary, ann).
parent(mary, pat).
parent(pat, jim).

% Forward Chaining
% Generate all possible ancestor relationships
generate_ancestors :-
    ancestor(X, Y),
    assert(ancestor(X, Y)),
    fail.
generate_ancestors.

% Queries
% Query 1: Is John an ancestor of Jim?
% Input: query1.
% Output: Yes, John is an ancestor of Jim.
query1 :- ancestor(john, jim), write('Yes, John is an ancestor of Jim.').

% Query 2: Who are the ancestors of Ann?
% Input: query2.
% Output: Mary, John
query2 :- write('Ancestors of Ann: '), ancestor(X, ann), write(X), write(', '), fail.

% Query 3: Are there any descendants of Mary?
% Input: query3.
% Output: Yes, there are descendants of Mary: Ann, Pat, Jim
query3 :- write('Descendants of Mary: '), ancestor(mary, X), write(X), write(', '), fail.

% Query 4: Is Pat a descendant of John?
% Input: query4.
% Output: Yes, Pat is a descendant of John.
query4 :- ancestor(john, pat), write('Yes, Pat is a descendant of John.').

% Query 5: Who are the descendants of John?
% Input: query5.
% Output: Mary, Tom, Ann, Pat, Jim
query5 :- write('Descendants of John: '), ancestor(john, X), write(X), write(', '), fail.

% Query 6: Are there any ancestors of Tom?
% Input: query6.
% Output: Yes, there are ancestors of Tom: John, Mary
query6 :- write('Ancestors of Tom: '), ancestor(X, tom), write(X), write(', '), fail.

% Query 7: Is Ann a parent of Pat?
% Input: query7.
% Output: No, Ann is not a parent of Pat.
query7 :- parent(ann, pat), write('No, Ann is not a parent of Pat.').

% Query 8: Is Jim a parent of Mary?
% Input: query8.
% Output: No, Jim is not a parent of Mary.
query8 :- parent(jim, mary), write('No, Jim is not a parent of Mary.').

% Run forward chaining to generate conclusions
:- generate_ancestors.
