# Google-Page-Rank
## Prerequisite Knowledge:
PageRank (developed by Larry Page and Sergey Brin) revolutionized web search by generating a ranked list of web pages based on the underlying connectivity of the web.
The PageRank algorithm is based on an ideal random web user who, when reaching a page, goes to the next page by clicking on a link. The user has equal probability of clicking any link on the page and, when reaching a page with no links, has equal probability of moving to any other page by typing in its URL. In addition, the user may occasionally choose to type in a random URL instead of following the links on a page. 
websites most linked to is to have more visitors and, this algorithm ranks sites of having more users in the browsing process.
## Code Explanation:
1- we make a matrix L where the rows represents how likely to enter a website and 
col represents the probability of leavine website => sum =1
2- rank vector r that represents the rank of website x which is the sum of the ranks of all the pages which link
to it, weighted by their specific link probability taken from matrix L
hence, r = Lr (all the ranks are equally and normalise them by the total number of webpages)
update the values in r until, eventually, r stops changing ( convergence ), then r is an eigen vector of matrix L of eigen value of 1.
## Function Refinement
we use a damping parameter d to quikly converge.
d is something between 0 and 1 is to control between speed and stability.
d=1 <- user always follows a link.
d=0 <- user always visit a random webpage and webpages are equally ranked.


