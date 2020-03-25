from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import sys
application = Flask(__name__)


searchResults = []
indices = []

searchTerm = ""

movies = [
 
  {
 "id": 0,
 "name": "The Shawshank Redemption ",
 "description": "The Shawshank Redemption is a 1994 American drama film written and directed by Frank Darabont, based on the 1982 Stephen King novella Rita Hayworth and Shawshank Redemption. It tells the story of banker Andy Dufresne (Tim Robbins), who is sentenced to life in Shawshank State Penitentiary for the murders of his wife and her lover, despite his claims of innocence. Over the following two decades, he befriends a fellow prisoner, contraband smuggler Ellis Redding (Morgan Freeman), and becomes instrumental in a money-laundering operation led by the prison warden Samuel Norton (Bob Gunton). William Sadler, Clancy Brown, Gil Bellows, and James Whitmore appear in supporting roles.",
 "rating": 9.3, 
 "url": "https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX67_CR0,0,67,98_AL_.jpg", 
 "stars": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
 "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]

 }, 
  {
 "id": 1,
 "name": "The Godfather  ",
 "description": "The Godfather is a 1972 American crime film directed by Francis Ford Coppola and produced by Albert S. Ruddy, based on Mario Puzo's best-selling novel of the same name. It is the first installment in The Godfather trilogy. It stars Marlon Brando and Al Pacino as the father and son of a fictional New York crime family. The story, spanning 1945 to 1955, chronicles the family under the patriarch Vito Corleone (Brando), focusing on the transformation of the son Michael Corleone (Pacino), raised to have a life outside of crime, from reluctant family outsider to ruthless mafia boss.",
 "rating": 9.2, 
 "url": "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY98_CR1,0,67,98_AL_.jpg", 
 "stars": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 },
 {
 "id": 2,
 "name": "The Dark Knight",
 "description": "The Dark Knight is a 2008 superhero film directed, co-produced, and co-written by Christopher Nolan. Based on the DC Comics character Batman, the film is the second installment of Nolan's The Dark Knight Trilogy and a sequel to 2005's Batman Begins, starring Christian Bale and supported by Michael Caine, Heath Ledger, Gary Oldman, Aaron Eckhart, Maggie Gyllenhaal, and Morgan Freeman. In the film, Bruce Wayne / Batman (Bale), Police Lieutenant James Gordon (Oldman) and District Attorney Harvey Dent (Eckhart) form an alliance to dismantle organized crime in Gotham City, but are menaced by an anarchistic mastermind known as the Joker (Ledger), who seeks to undermine Batman's influence and turn the city to chaos.",
 "rating": 9.0,
 "url": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY209_CR0,0,140,209_AL_.jpg", 
 "stars": ["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Michael Caine"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 },
  {
 "id": 3,
 "name": "The Godfather: Part II ",
 "description": "The Godfather Part II is a 1974 American epic crime film produced and directed by Francis Ford Coppola from the screenplay co-written with Mario Puzo, starring Al Pacino and Robert De Niro. It is the second installment in The Godfather trilogy. Partially based on Puzo's 1969 novel The Godfather, the film is both sequel and prequel to The Godfather, presenting parallel dramas: one picks up the 1958 story of Michael Corleone (Pacino), the new Don of the Corleone crime family, protecting the family business in the aftermath of an attempt on his life; the prequel covers the journey of his father, Vito Corleone (De Niro), from his Sicilian childhood to the founding of his family enterprise in New York City.Following the success of the first film, Paramount Pictures began developing a follow up to the film, with much of the same cast and crew returning. Coppola, who was given more control on the film, had wanted to make both a sequel and a prequel to the film to tell the story of the rise of Vito and the fall of Michael.",
 "rating": 9.0,
 "url": "https://m.media-amazon.com/images/M/MV5BMWMwMGQzZTItY2JlNC00OWZiLWIyMDctNDk2ZDQ2YjRjMWQ0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY98_CR1,0,67,98_AL_.jpg", 
 "stars": ["Al Pacino", "Robert De Niro", "Robert Duvall", "Diane Keaton"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 },


 {
 "id": 4,
 "name": "The Lord of the Rings: The Return of the King  ",
 "description": "The Lord of the Rings is an epic[1] high-fantasy novel written by English author and scholar J. R. R. Tolkien. The story began as a sequel to Tolkien's 1937 fantasy novel The Hobbit, but eventually developed into a much larger work. Written in stages between 1937 and 1949, The Lord of the Rings is one of the best-selling novels ever written, with over 150 million copies sold.[2]The title of the novel refers to the story's main antagonist, the Dark Lord Sauron,[a] who had in an earlier age created the One Ring to rule the other Rings of Power as the ultimate weapon in his campaign to conquer and rule all of Middle-earth. From quiet beginnings in the Shire, a hobbit land not unlike the English countryside, the story ranges across Middle-earth, following the course of the War of the Ring through the eyes of its characters, most notably the hobbits Frodo, Sam, Merry and Pippin.",
 "rating": 8.9, 
 "url": "https://m.media-amazon.com/images/M/MV5BNzA5ZDNlZWMtM2NhNS00NDJjLTk4NDItYTRmY2EwMWZlMTY3XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX67_CR0,0,67,98_AL_.jpg", 
 "stars": ["Elijah Wood", "Viggo Mortensen", "Ian McKellen", "Orlando Bloom"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 }, 

 {
 "id": 5,
 "name": "Pulp Fiction ",
 "description": "Pulp Fiction is a 1994 American crime film written and directed by Quentin Tarantino, who conceived it with Roger Avary.[5] Starring John Travolta, Samuel L. Jackson, Bruce Willis, Tim Roth, Ving Rhames, and Uma Thurman, it tells several stories of criminal Los Angeles. The title refers to the pulp magazines and hardboiled crime novels popular during the mid-20th century, known for their graphic violence and punchy dialogue.Tarantino wrote Pulp Fiction in 1992 and 1993, incorporating scenes that Avary originally wrote for True Romance (1993). Its plot occurs out of chronological order. The film is also self-referential from its opening moments, beginning with a title card that gives two dictionary definitions of . Considerable screen time is devoted to monologues and casual conversations with eclectic dialogue revealing each character's perspectives on several subjects, and the film features an ironic combination of humor and strong violence. TriStar Pictures reportedly turned down the script as too demented. Miramax co-chairman Harvey Weinstein was enthralled, however, and the film became the first that Miramax fully financed.",
 "rating": 8.9, 
 "url": "https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY209_CR2,0,140,209_AL_.jpg", 
 "stars": ["John Travolta", "Uma Thurman", "Samuel L. Jackson", "Bruce Willis"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 }, 

  {
 "id": 6,
 "name": "Schindler's List  ",
 "description": "Schindler's List is a 1993 American historical drama film directed and co-produced by Steven Spielberg and written by Steven Zaillian. It is based on the novel Schindler's Ark by Australian novelist Thomas Keneally. The film follows Oskar Schindler, a Sudeten German businessman, who saved more than a thousand mostly Polish-Jewish refugees from the Holocaust by employing them in his factories during World War II. It stars Liam Neeson as Schindler, Ralph Fiennes as SS officer Amon Göth, and Ben Kingsley as Schindler's Jewish accountant Itzhak Stern.Ideas for a film about the Schindlerjuden (Schindler Jews) were proposed as early as 1963. Poldek Pfefferberg, one of the Schindlerjuden, made it his life's mission to tell Schindler's story. Spielberg became interested when executive Sidney Sheinberg sent him a book review of Schindler's Ark. Universal Pictures bought the rights to the novel, but Spielberg, unsure if he was ready to make a film about the Holocaust, tried to pass the project to several directors before deciding to direct it.",
 "rating": 8.9, 
 "url": "https://m.media-amazon.com/images/M/MV5BNDE4OTMxMTctNmRhYy00NWE2LTg3YzItYTk3M2UwOTU5Njg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX67_CR0,0,67,98_AL_.jpg", 
 "stars": ["Liam Neeson", "Ralph Fiennes", "Ben Kingsley", "Caroline Goodall"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 }, 

  {
 "id": 7,
 "name": "12 Angry Men  ",
 "description": "In the murder trial of a teenaged boy from a city slum, accused of murdering his father, the judge gives her instructions to the jury: a non-unanimous verdict will force a mistrial, and a guilty verdict will be accompanied by a mandatory death sentence. The jury of twelve retires to the jury room.An initial vote is taken and eleven jurors vote for conviction. Juror 8, the lone dissenter, states that the evidence is circumstantial and the boy deserves a fair deliberation. He questions the testimony of the two witnesses, and the fact that the switchblade used in the murder is not as unusual as the testimony indicates producing an identical knife from his pocket.Juror 8 proposes another vote by secret ballot – if the other jurors vote guilty unanimously, he will acquiesce, but if at least one votes they will continue deliberating. Only Juror 9 changes his vote, respecting Juror 8’s motives and feeling his points deserve further discussion.",
 "rating": 8.9, 
 "url": "https://m.media-amazon.com/images/M/MV5BMWU4N2FjNzYtNTVkNC00NzQ0LTg0MjAtYTJlMjFhNGUxZDFmXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_UX67_CR0,0,67,98_AL_.jpg", 
 "stars": ["Henry Fonda", "Lee J. Cobb", "Martin Balsam", "John Fiedler"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 }, 

  {
 "id": 8,
 "name": "Inception ",
 "description": "Inception is a 2010 psychological science fiction action film[3] written and directed by Christopher Nolan, who also produced the film with his wife, Emma Thomas. The film stars Leonardo DiCaprio as a professional thief who steals information by infiltrating the subconscious of his targets. He is offered a chance to have his criminal history erased as payment for the implantation of another person's idea into a target's subconscious.[4] The ensemble cast includes Ken Watanabe, Joseph Gordon-Levitt, Marion Cotillard, Ellen Page, Tom Hardy, Dileep Rao, Cillian Murphy, Tom Berenger, and Michael Caine.",
 "rating": 8.8, 
 "url": "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_UX67_CR0,0,67,98_AL_.jpg", 
 "stars": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page", "Ken Watanabe"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 }, 

  {
 "id": 9,
 "name": "Fight Club   ",
 "description": "Fight Club is a 1999 American film directed by David Fincher and starring Brad Pitt, Edward Norton, and Helena Bonham Carter. It is based on the 1996 novel of the same name by Chuck Palahniuk. Norton plays the unnamed narrator, who is discontented with his white-collar job. He forms a fight clubwith soap salesman Tyler Durden (Pitt), and becomes embroiled in a relationship with him and a destitute woman, Marla Singer (Bonham Carter). Palahniuk's novel was optioned by Fox 2000 Pictures producer Laura Ziskin, who hired Jim Uhls to write the film adaptation. Fincher was selected because of his enthusiasm for the story. He developed the script with Uhls and sought screenwriting advice from the cast and others in the film industry. He and the cast compared the film to Rebel Without a Cause (1955) and The Graduate (1967), with a theme of conflict between Generation X and the value system of advertising.[4][5]",
 "rating": 8.8, 
 "url": "https://m.media-amazon.com/images/M/MV5BMmEzNTkxYjQtZTc0MC00YTVjLTg5ZTEtZWMwOWVlYzY0NWIwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX67_CR0,0,67,98_AL_.jpg", 
 "stars": ["Brad Pitt", "Edward Norton", "Meat Loaf", "Zach Grenier"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 }, 

  {
 "id": 10,
 "name": " The Lord of the Rings: The Fellowship of the Ring   ",
 "description": "The Lord of the Rings: The Fellowship of the Ring is a 2001 epic fantasy adventure film directed by Peter Jackson, based on the first volume of J. R. R. Tolkien's The Lord of the Rings. The film is the first installment in The Lord of the Rings trilogy and was produced by Barrie M. Osborne, Jackson, Fran Walsh and Tim Sanders, and written by Walsh, Philippa Boyens and Jackson. The film features an ensemble cast including Elijah Wood, Ian McKellen, Liv Tyler, Viggo Mortensen, Sean Astin, Cate Blanchett, John Rhys-Davies, Billy Boyd, Dominic Monaghan, Orlando Bloom, Christopher Lee, Hugo Weaving, Sean Bean, Ian Holm, and Andy Serkis. It was followed by The Two Towers (2002) and The Return of the King (2003).",
 "rating": 8.8, 
 "url": "https://m.media-amazon.com/images/M/MV5BNDE4OTMxMTctNmRhYy00NWE2LTg3YzItYTk3M2UwOTU5Njg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX67_CR0,0,67,98_AL_.jpg", 
 "stars": ["Elijah Wood", "Ian McKellen", "Orlando Bloom", "Sean Bean"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 }, 

  {
 "id": 11,
 "name": "Forrest Gump   ",
 "description": "Forrest Gump is a 1994 American magical realism comedy-drama film directed by Robert Zemeckis and written by Eric Roth. It is based on the 1986 novel of the same name by Winston Groom, and stars Tom Hanks, Robin Wright, Gary Sinise, Mykelti Williamson, and Sally Field. The story depicts several decades in the life of Forrest Gump (Hanks), a slow-witted but kind-hearted man from Alabama who witnesses and unwittingly influences several defining historical events in the 20th century United States. The film differs substantially from the novel.",
 "rating": 8.8, 
 "url": "https://m.media-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY98_CR0,0,67,98_AL_.jpg", 
 "stars": ["Tom Hanks", "Robin Wright", "Gary Sinise", "Sally Field"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 }, 

  {
 "id": 12,
 "name": "The Good, the Bad and the Ugly  ",
 "description": "The film is known for Leone's use of long shots and close-up cinematography, as well as his distinctive use of violence, tension, and stylistic gunfights. The plot revolves around three gunslingers competing to find fortune in a buried cache of Confederate gold amid the violent chaos of the American Civil War (specifically the New Mexico Campaign in 1862), while participating in many battles and duels along the way.[11] The film was the third collaboration between Leone and Clint Eastwood, and the second with Lee Van Cleef.",
 "rating": 8.8, 
 "url": "https://m.media-amazon.com/images/M/MV5BNDE4OTMxMTctNmRhYy00NWE2LTg3YzItYTk3M2UwOTU5Njg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX67_CR0,0,67,98_AL_.jpg", 
 "stars": ["Clint Eastwood", "Eli Wallach", "Lee Van Cleef", "Aldo Giuffrè"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 },  

  {
 "id": 13,
 "name": "The Lord of the Rings: The Two Towers  ",
 "description": "The Lord of the Rings: The Two Towers is a 2002 epic fantasy adventure film directed by Peter Jackson, based on the second volume of J. R. R. Tolkien's The Lord of the Rings. The film is the second instalment in The Lord of the Rings trilogy and was produced by Barrie M. Osborne, Fran Walsh and Jackson, and written by Walsh, Philippa Boyens, Stephen Sinclair and Jackson. The film features an ensemble cast including Elijah Wood, Ian McKellen, Liv Tyler, Viggo Mortensen, Sean Astin, Cate Blanchett, John Rhys-Davies, Bernard Hill, Christopher Lee, Billy Boyd, Dominic Monaghan, Orlando Bloom, Hugo Weaving, Miranda Otto, David Wenham, Brad Dourif, Karl Urban and Andy Serkis. It was preceded by The Fellowship of the Ring (2001) and followed by The Return of the King (2003).",
 "rating": 8.7, 
 "url": "https://m.media-amazon.com/images/M/MV5BNGE5MzIyNTAtNWFlMC00NDA2LWJiMjItMjc4Yjg1OWM5NzhhXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY98_CR0,0,67,98_AL_.jpg", 
 "stars": ["Elijah Wood", "Ian McKellen", "Viggo Mortensen", "Orlando Bloom"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 },  

  {
 "id": 14,
 "name": "The Matrix   ",
 "description": "The series features a cyberpunk story of the technological fall of man, in which the creation of artificial intelligence led way to a race of self-aware machines that imprisoned mankind in a virtual reality system—the Matrix—to be farmed as a power source. Every now and then, some of the prisoners manage to break free from the system and, considered a threat, become pursued by the artificial intelligence both inside and outside of it. The films focus on the plight of Neo (Keanu Reeves), Trinity (Carrie-Anne Moss), and Morpheus (Laurence Fishburne) trying to free humanity from the system while pursued by its guardians, such as Agent Smith (Hugo Weaving). The story incorporates references to numerous philosophical, religious, or spiritual ideas, among others the dilemma of choice vs. control, the brain in a vat thought experiment, messianism, and the concepts of inter-dependency and love. Influences include the principles of mythology, anime, and Hong Kong action films (particularly and martial arts movies). The film series is notable for its use of heavily choreographed action sequenlow motion effects, which revolutionized action films to come.",
 "rating": 8.7, 
 "url": "https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX67_CR0,0,67,98_AL_.jpg", 
 "stars": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss", "Hugo Weaving"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 },   

   {
 "id": 15,
 "name": "Goodfellas",
 "description": "Scorsese initially titled the film Wise Guy and postponed making it; later, he and Pileggi changed the title to Goodfellas. To prepare for their roles in the film, Robert De Niro, Joe Pesci and Ray Liotta often spoke with Pileggi, who shared research material left over from writing the book. According to Pesci, improvisation and ad-libbing came out of rehearsals wherein Scorsese gave the actors freedom to do whatever they wanted. The director made transcripts of these sessions, took the lines he liked most and put them into a revised script, which the cast worked from during principal photography.",
 "rating": 8.7, 
 "url": "https://m.media-amazon.com/images/M/MV5BY2NkZjEzMDgtN2RjYy00YzM1LWI4ZmQtMjIwYjFjNmI3ZGEwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX67_CR0,0,67,98_AL_.jpg", 
 "stars": ["Robert De Niro", "Ray Liotta", "Joe Pesci", "Lorraine Bracco"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 },

  {
 "id": 16,
 "name": "Star Wars: Episode V - The Empire Strikes Back    ",
 "description": "The Empire Strikes Back, also known as Star Wars: Episode V – The Empire Strikes Back, is a 1980 American epic space opera film directed by Irvin Kershner and written by Leigh Brackett and Lawrence Kasdan, based on a story by George Lucas. Produced by Lucasfilm, it is the second film in the Star Wars film series (albeit the fifth chronologically) and the sequel to Star Wars (1977).[a] Set three years after the events of the first film, the Galactic Empire, under the leadership of Darth Vader and the Emperor, pursues Luke Skywalker and the rest of the Rebel Alliance. While Vader relentlessly pursues Luke's friends—Han Solo, Princess Leia, Chewbacca, and C-3PO—Luke studies the Force under Jedi Master Yoda. The ensemble cast includes Mark Hamill, Harrison Ford, Carrie Fisher, Billy Dee Williams, Anthony Daniels, David Prowse, Kenny Baker, Peter Mayhew, and Frank Oz.",
 "rating": 8.7, 
 "url": "https://m.media-amazon.com/images/M/MV5BYmU1NDRjNDgtMzhiMi00NjZmLTg5NGItZDNiZjU5NTU4OTE0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX67_CR0,0,67,98_AL_.jpg", 
 "stars": ["Mark Hamill", "Harrison Ford", "Carrie Fisher", "Billy Dee Williams"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 }, 

  {
 "id": 17,
 "name": "One Flew Over the Cuckoo's Nest   ",
 "description": "One Flew Over the Cuckoo's Nest is a 1975 American comedy-drama film directed by Miloš Forman, based on the 1962 novel One Flew Over the Cuckoo's Nest by Ken Kesey and the play version adapted from the novel by Dale Wasserman. The film stars Jack Nicholson as Randle McMurphy, a new patient at a mental institution, and features a supporting cast of Louise Fletcher, William Redfield, Will Sampson, Sydney Lassick, Brad Dourif, Danny DeVito and Christopher Lloyd in his film debut.",
 "rating": 8.7, 
 "url": "https://m.media-amazon.com/images/M/MV5BZjA0OWVhOTAtYWQxNi00YzNhLWI4ZjYtNjFjZTEyYjJlNDVlL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX67_CR0,0,67,98_AL_.jpg", 
 "stars": ["Jack Nicholson", "Louise Fletcher", "Will Sampson", "Michael Berryman"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 }, 

  {
 "id": 18,
 "name": "Harakiri    ",
 "description": "The practice was not standardised until the 17th century. In the 12th and 13th centuries, such as with the seppuku of Minamoto no Yorimasa, the practice of a kaishakunin (idiomatically,had not yet emerged, thus the rite was considered far more painful. Seppuku's defining characteristic was plunging either the tachi (longsword), wakizashi (shortsword) or tantō (knife) into the gut and slicing the abdomen horizontally. In the absence of a kaishakunin, the samurai would then remove the blade, and stab himself in the throat, or fall (from a standing position) with the blade positioned against his heart.During the Edo Period (1600–1867), carrying out seppuku came to involve a detailed ritual. This was usually performed in front of spectators if it was a planned seppuku, not one performed on a battlefield. A samurai was bathed, dressed in white robes, and served his favorite foods for a last meal. When he had finished, the knife and cloth were placed on another sanbo and given to the warrior. Dressed ceremonially, with his sword placed in front of him and sometimes seated on special clothes, the warrior would prepare for death by writing a death poem. He would be dressed in the shini-shōzoku, a completely white kimono worn for death",
 "rating": 8.7, 
 "url": "https://m.media-amazon.com/images/M/MV5BYjBmYTQ1NjItZWU5MS00YjI0LTg2OTYtYmFkN2JkMmNiNWVkXkEyXkFqcGdeQXVyMTMxMTY0OTQ@._V1_UY98_CR2,0,67,98_AL_.jpg", 
 "stars": ["Tatsuya Nakadai", "Akira Ishihama", "Shima Iwashita", "Tetsurô Tanba"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 }, 

  {
 "id": 19,
 "name": "Joker   ",
 "description": "Joker is a 2019 American psychological thriller film directed and produced by Todd Phillips, who co-wrote the screenplay with Scott Silver. The film, based on DC Comics characters, stars Joaquin Phoenix as the Joker and provides a possible origin story for the character. Set in 1981, it follows Arthur Fleck, a failed stand-up comedian whose descent into insanity and nihilism inspires a violent counter-cultural revolution against the wealthy in a decaying Gotham City. Robert De Niro, Zazie Beetz, Frances Conroy, Brett Cullen, Glenn Fleshler, Bill Camp, Shea Whigham, and Marc Maron appear in supporting roles. Joker was produced by Warner Bros. Pictures, DC Films, and Joint Effort, in association with Bron Creative and Village Roadshow Pictures, and distributed by Warner Bros.",
 "rating": 8.6, 
 "url": "https://m.media-amazon.com/images/M/MV5BNGVjNWI4ZGUtNzE0MS00YTJmLWE0ZDctN2ZiYTk2YmI3NTYyXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX67_CR0,0,67,98_AL_.jpg", 
 "stars": ["Joaquin Phoenix", "Robert De Niro", "Zazie Beetz", "Frances Conroy"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 }, 

 {
 "id": 20,
 "name": "Parasite   ",
 "description": "Parasite (Korean: 기생충; RR: Gisaengchung) is a 2019 South Korean black comedy thriller film directed by Bong Joon-ho, who also co-wrote the screenplay with Han Jin-won. It stars Song Kang-ho, Lee Sun-kyun, Cho Yeo-jeong, Choi Woo-shik, Park So-dam, and Jang Hye-jin and follows the members of a poor family who scheme to become employed by a wealthy family by infiltrating their household and posing as unrelated, highly qualified individuals.Parasite premiered at the 2019 Cannes Film Festival on 21 May 2019, where it became the first South Korean film to win the Palme d'Or and the first film to win with a unanimous vote since Blue Is the Warmest Colour at the 2013 Festival. It was then released in South Korea by CJ Entertainment on 30 May 2019. The film received critical acclaim, with praise drawn towards its screenplay, Bong's direction, acting, social commentary, cinematography, editing and production values, and has been featured in multiple listings of the best films of the 2010s. It has grossed over $236 million worldwide on a production budget of about $11 million, becoming one of the highest-grossing South Korean films.",
 "rating": 8.6, 
 "url": "https://m.media-amazon.com/images/M/MV5BYWZjMjk3ZTItODQ2ZC00NTY5LWE0ZDYtZTI3MjcwN2Q5NTVkXkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_UX67_CR0,0,67,98_AL_.jpg", 
 "stars": ["Kang-ho Song", "Sun-kyun Lee", "Yeo-jeong Jo", "Woo-sik Choi"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 }, 

 {
 "id": 21,
 "name": " Interstellar   ",
 "description": "Brothers Christopher and Jonathan Nolan wrote the screenplay, which had its origins in a script Jonathan developed in 2007. Christopher produced Interstellar with his wife, Emma Thomas, through their production company Syncopy, and with Lynda Obst through Lynda Obst Productions. Caltech theoretical physicist Kip Thorne was an executive producer, acted as scientific consultant, and wrote a tie-in book, The Science of Interstellar. Paramount Pictures, Warner Bros., and Legendary Pictures co-financed the film. Cinematographer Hoyte van Hoytema shot it on 35 mm in anamorphic format and IMAX 70 mm. Principal photography began in late 2013 and took place in Alberta (Canada), Iceland and Los Angeles. Interstellar uses extensive practical and miniature effects and the company Double Negative created additional digital effects.",
 "rating": 8.6, 
 "url": "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX67_CR0,0,67,98_AL_.jpg", 
 "stars": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain", "Mackenzie Foy"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 },

 {
 "id": 22,
 "name": "City of God",
 "description": "City of God (Portuguese: Cidade de Deus) is a 2002 Brazilian crime film co-directed by Fernando Meirelles and Kátia Lund, released in its home country in 2002 and worldwide in 2003. The story was adapted by Bráulio Mantovani from the 1997 novel of the same name written by Paulo Lins, but the plot is loosely based on real events. It depicts the growth of organized crime in the Cidade de Deus suburb of Rio de Janeiro, between the end of the 1960s and the beginning of the 1980s, with the closure of the film depicting the war between the drug dealer Li'l Zé and vigilante-turned-criminal Knockout Ned. The tagline is",
 "rating": 8.6, 
 "url": "https://m.media-amazon.com/images/M/MV5BNGVjNWI4ZGUtNzE0MS00YTJmLWE0ZDctN2ZiYTk2YmI3NTYyXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX67_CR0,0,67,98_AL_.jpg", 
 "stars": ["Alexandre Rodrigues", "Leandro Firmino", "Matheus Nachtergaele", "Phellipe Haagensen"],
  "user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 },

 {
 "id": 23,
 "name": "Spirited Away   ",
 "description": "Spirited Away (Japanese: 千と千尋の神隠し, Hepburn: Sen to Chihiro no Kamikakushi,  Spiriting Awa) is a 2001 Japanese animated coming-of-age fantasy film written and directed by Hayao Miyazaki, animated by Studio Ghibli for Tokuma Shoten, Nippon Television Network, Dentsu, Buena Vista Home Entertainment, Tohokushinsha Film and Mitsubishi, and distributed by Toho.[6] The film stars Rumi Hiiragi, Miyu Irino, Mari Natsuki, Takeshi Naito, Yasuko Sawaguchi, Tsunehiko Kamijō, Takehiko Ono, and Bunta Sugawara. Spirited Away tells the story of Chihiro Ogino (Hiiragi), a 10-year-old girl who, while moving to a new neighbourhood, enters the world of Kami (spirits) of Japanese Shinto folklore.[7] After her parents are turned into pigs by the witch Yubaba (Natsuki), Chihiro takes a job working in Yubaba's bathhouse to find a way to free herself and her parents and return to the human world.",
 "rating": 8.6, 
 "url": "https://m.media-amazon.com/images/M/MV5BNmU5OTQ0OWQtOTY0OS00Yjg4LWE1NDYtNDRhYWMxYWY4OTMwXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UY67_CR1,0,45,67_AL_.jpg", 
 "stars": ["Daveigh Chase", "Suzanne Pleshette", "Miyu Irino", "Rumi Hiiragi"],
"user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 }, 

 {
 "id": 24,
 "name": "Saving Private Ryan  ",
 "description": "Saving Private Ryan is a 1998 American epic war film directed by Steven Spielberg and written by Robert Rodat. Set during the Invasion of Normandy in World War II, the film is notable for its graphic portrayal of war and for the intensity of its opening 27 minutes, which includes a depiction of the Omaha Beach assault during the Normandy landings. The film follows United States Army Rangers Captain John H. Miller (Tom Hanks) and his squad (Tom Sizemore, Edward Burns, Barry Pepper, Giovanni Ribisi, Vin Diesel, Adam Goldberg, and Jeremy Davies) as they search for a paratrooper, Private First Class James Francis Ryan (Matt Damon), the last surviving brother of three servicemen killed in action. The film is a co-production between DreamWorks Pictures, Paramount Pictures, Amblin Entertainment, and Mutual Film Company, with DreamWorks distributing the film in North America while Paramount released the film internationally.",
 "rating": 8.6, 
 "url": "https://m.media-amazon.com/images/M/MV5BZjhkMDM4MWItZTVjOC00ZDRhLThmYTAtM2I5NzBmNmNlMzI1XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UY67_CR0,0,45,67_AL_.jpg", 
 "stars": ["Tom Hanks", "Matt Damon", "Tom Sizemore", "Edward Burns"],
"user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 }, 

 {
 "id": 25,
 "name": "The Green Mile   ",
 "description": "Paul Edgecomb (Tom Hanks) walked the mile with a variety of cons. He had never encountered someone like John Coffey (Michael Clarke Duncan), a massive black man convicted of brutally killing a pair of young sisters. Coffey had the size and strength to kill anyone, but not the demeanor. Beyond his simple, naive nature and a deathly fear of the dark, Coffey seemed to possess a prodigious, supernatural gift. Paul began to question whether Coffey was truly guilty of murdering the two girls.",
 "rating": 8.6, 
 "url": "https://m.media-amazon.com/images/M/MV5BMTUxMzQyNjA5MF5BMl5BanBnXkFtZTYwOTU2NTY3._V1_UY67_CR0,0,45,67_AL_.jpg", 
 "stars": ["Tom Hanks", "Michael Clarke Duncan", "David Morse", "Bonnie Hunt"],
"user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 }, 

 {
 "id": 26,
 "name": "Life Is Beautiful    ",
 "description": "Life Is Beautiful (Italian: La vita è bella, Italian pronunciation: [la ˈviːta ˈɛ ˈbɛlla]) is a 1997 Italian comedy-drama film directed by and starring Roberto Benigni, who co-wrote the film with Vincenzo Cerami. Benigni plays Guido Orefice, a Jewish Italian bookshop owner, who employs his fertile imagination to shield his son from the horrors of internment in a Nazi concentration camp. The film was partially inspired by the book In the End, I Beat Hitler by Rubino Romeo Salmonì and by Benigni's father, who spent two years in a German labour camp during World War II.The film was a critical and financial success. It grossed over $230 million worldwide, becoming one of the highest-grossing non-English language movies of all time,[4] and received widespread acclaim (despite some criticisms of using the subject matter for comedic purposes). It won the Grand Prix at the 1998 Cannes Film Festival, nine David di Donatello Awards (including Best Film), five Nastro d'Argento Awards in Italy, two European Film Awards, and three Academy Awards (including Best Foreign Language Film and Best Actor for Benigni).",
 "rating": 8.6, 
 "url": "https://m.media-amazon.com/images/M/MV5BYmJmM2Q4NmMtYThmNC00ZjRlLWEyZmItZTIwOTBlZDQ3NTQ1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX67_CR0,0,67,98_AL_.jpg", 
 "stars": ["Roberto Benigni", "Nicoletta Braschi", "Giorgio Cantarini", "Giustino Durano"],
"user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 }, 

 {
 "id": 27,
 "name": "Se7en   ",
 "description": "Seven (stylized as SE7EN) is a 1995 American crime thriller film directed by David Fincher and written by Andrew Kevin Walker. It stars Brad Pitt, Morgan Freeman, Gwyneth Paltrow, Kevin Spacey and John C. McGinley. The film tells the story of David Mills, a detective who partners with the retiring William Somerset to track down a serial killer who uses the seven deadly sins as a motif in his murders.The screenplay was influenced by the time Walker spent in New York City trying to make it as a writer. Principal photography took place in Los Angeles, with the last scene filmed near Lancaster, California. The film's budget was $33 million.",
 "rating": 8.6, 
 "url": "https://m.media-amazon.com/images/M/MV5BOTUwODM5MTctZjczMi00OTk4LTg3NWUtNmVhMTAzNTNjYjcyXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX67_CR0,0,67,98_AL_.jpg", 
 "stars": ["Morgan Freeman", "Brad Pitt", "Kevin Spacey", "Andrew Kevin Walker"],
"user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 }, 

 {
 "id": 28,
 "name": "The Silence of the Lambs  ",
 "description": "The Silence of the Lambs is a 1991 American psychological horror[3] film directed by Jonathan Demme from a screenplay written by Ted Tally, adapted from Thomas Harris's 1988 novel of the same name. The film stars Jodie Foster, Anthony Hopkins, Scott Glenn, Ted Levine, and Anthony Heald.[4] In the film, Clarice Starling, a young FBI trainee, seeks the advice of the imprisoned Dr. Hannibal Lecter, a brilliant psychiatrist and cannibalistic serial killer to apprehend another serial killer, known only as who skins his female victims' corpses. The novel was Harris's first and second respectively to feature the characters of Starling and Lecter, and was the second adaptation of a Harris novel to feature Lecter, preceded by the Michael Mann-directed Manhunter (1986).",
 "rating": 8.6, 
 "url": "https://m.media-amazon.com/images/M/MV5BNGVjNWI4ZGUtNzE0MS00YTJmLWE0ZDctN2ZiYTk2YmI3NTYyXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX67_CR0,0,67,98_AL_.jpg", 
 "stars": ["Jodie Foster", "Anthony Hopkins", "Lawrence A. Bonney", "Kasi Lemmons"],
"user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 }, 

 {
 "id": 29,
 "name": "Star Wars: Episode IV ",
 "description": "Star Wars: Episode III – Revenge of the Sith is a 2005 American epic space-opera film written and directed by George Lucas. It stars Ewan McGregor, Natalie Portman, Hayden Christensen, Ian McDiarmid, Samuel L. Jackson, Christopher Lee, Anthony Daniels, Kenny Baker and Frank Oz. It is the final installment in the Star Wars prequel trilogy, the third chapter in the Skywalker saga and the sixth Star Wars film to be released overall.Revenge of the Sith is set three years after the onset of the Clone Wars, established in Star Wars: Episode II – Attack of the Clones (2002). The Jedi are spread across the galaxy, leading a large-scale war against the Separatists. After Count Dooku is killed, the Jedi Council dispatches Obi-Wan Kenobi to eliminate General Grievous, the leader of the Separatist army, and put an end to the war. Meanwhile, after having premonitions of his wife Padmé Amidala dying in childbirth, Anakin Skywalker is tasked by the Council to spy on Palpatine, the Supreme Chancellor of the Galactic Republic and, secretly, a Sith lord known as Darth Sidious. Palpatine manipulates Anakin into turning to the dark side of the Force and becoming his apprentice, Darth Vader, with wide-ranging consequences for the galaxy.",
 "rating": 8.6, 
 "url": "https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX67_CR0,0,67,98_AL_.jpg", 
 "stars": ["Mark Hamill", "Harrison Ford", "Carrie Fisher", "Alec Guinness"],
"user review": "", 
 "mark_as_deleted": "false", 
 "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
 }

 

 
 
  
]



current_id = len(movies)


for i in range(0,len(movies)):
    movies[i]["id"] = i; 
    movies[i]["user review"] = "User review"


for i in range(0,len(movies)):
    movies[i]["starsWithMarkedAsDeleted"].clear(); 
    for j in range(0, len(movies[i]["stars"])):
        movies[i]["starsWithMarkedAsDeleted"].append({"stars":movies[i]["stars"][j], "mark_as_deleted": "false"})

@application.route('/')
def hello(name=None):
    return render_template('home.html', movieResults = movies) 

@application.route('/create')
def createpage():
    return render_template('create.html', current_id = current_id) 


@application.route('/creating', methods=['GET', 'POST'])
def creating():
    
    global movies 
    global searchResults
    global current_id
    json_data = request.get_json()   
    
    # add new entry to array with 
    # a new id and the name the user sent in JSON
    movies.append(json_data)

    current_id = current_id + 1; 

    return jsonify("/view/" + str(current_id - 1)); 

    #send back the WHOLE array of data, so the client can redisplay it


@application.route('/search_results_link', methods=['GET', 'POST'])
def add_name():
    
    global movies 
    global searchResults
    global searchTerm
    searchResults = []
    json_data = request.get_json()   
    
    searchTerm = json_data
    # add new entry to array with 
    # a new id and the name the user sent in JSON
    for i in range (0,len(movies)):
        if json_data in movies[i]["name"]:
            searchResults.append(movies[i])

    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(searchResults = searchResults)


@application.route('/editing', methods=['GET', 'POST'])
def editing():
    
    global movies 
    global searchResults
    global searchTerm
    json_data = request.get_json()   
    
    newReview = json_data["searchTerm"]
    id = json_data["id"]

    # add new entry to array with 
    # a new id and the name the user sent in JSON
    movies[int(id)]["user review"] = newReview

    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(searchResults = searchResults)

@application.route('/editName', methods=['GET', 'POST'])
def editName():
    
    global movies 
    global searchResults
    global searchTerm
    json_data = request.get_json()   
    
    id = json_data["id"]
    nameSubmitted = json_data["nameSubmitted"]


    # add new entry to array with 
    # a new id and the name the user sent in JSON
    movies[int(id)]["name"] = nameSubmitted

    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(movies[int(id)])

@application.route('/deletestars', methods=['GET', 'POST'])
def deleteMovieStar():
    
    global movies 
    global searchResults
    global searchTerm
    json_data = request.get_json()   
    
    id = json_data["id"]
    idOfStar = json_data["idOfStar"]


    # add new entry to array with 
    # a new id and the name the user sent in JSON
    if movies[int(id)]["starsWithMarkedAsDeleted"][int(idOfStar)]["mark_as_deleted"] == "true":
     movies[int(id)]["starsWithMarkedAsDeleted"][int(idOfStar)]["mark_as_deleted"] = "false"
    

    else: 
        movies[int(id)]["starsWithMarkedAsDeleted"][int(idOfStar)]["mark_as_deleted"] = "true"


    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(movies[int(id)])

@application.route('/addReview', methods=['GET', 'POST'])
def editReview():
    
    global movies 
    global searchResults
    global searchTerm
    json_data = request.get_json()   
    
    id = json_data["id"]
    review = json_data["review"]


    # add new entry to array with 
    # a new id and the name the user sent in JSON
    movies[int(id)]["user review"] = review

    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(movies[int(id)])

@application.route('/delete', methods=['GET', 'POST'])
def delete():
    
    global movies 
    global searchResults
    global searchTerm
    global current_id
    json_data = request.get_json()




    
    index = int(json_data)
    

    del movies[index]
    current_id = current_id-1; 
    for i in range(0,len(movies)):
        movies[i]["id"] = i;

    searchResults = []
  

    for i in range (0,len(movies)):
        if searchTerm in movies[i]["name"]:
            searchResults.append(movies[i])
         

        else:
            for j in range (0,len(movies[i]["stars"])):
                if searchTerm in movies[i]["stars"][j]:
                    searchResults.append(movies[i])

    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(movies = movies, searchResults = searchResults)


@application.route('/view/<id>', methods=['GET', 'POST'])
def view(id = None):
    
    global movies 
    global searchResults
    actualid = int(id); 

    
    # add new entry to array with 
    # a new id and the name the user sent in JSON

    #send back the WHOLE array of data, so the client can redisplay it
    return render_template('view.html', data = movies[actualid], id = actualid) 


@application.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id = None):
    
    global movies 
    global searchResults
    actualid = int(id); 

    
    # add new entry to array with 
    # a new id and the name the user sent in JSON

    #send back the WHOLE array of data, so the client can redisplay it
    return render_template('edit.html', data = movies[actualid], id = actualid) 

@application.route('/search/<searchterm>', methods=['GET', 'POST'])
def search(searchterm = None):
    
    global movies 
    global searchResults
    global searchTerm
    global indices
    searchResults = []

    indices = []

    searchTerm = searchterm + ""

    for i in range (0,len(movies)):
        if searchTerm.lower() in movies[i]["name"].lower():
            searchResults.append(movies[i])
            indices.append({
                "index": ((movies[i]["name"].lower()).find(searchTerm.lower())),
                "type": "name",
                "elementOfStars": 0,
                "lengthOfSubstring": len(searchTerm.lower()),
                "lengthOfString": len(movies[i]["name"].lower()),
                "searchTerm": searchTerm
            })

        else:
            for j in range (0,len(movies[i]["stars"])):
                if searchTerm.lower() in movies[i]["stars"][j].lower() and not(movies[i] in searchResults):
                    searchResults.append(movies[i])
                    indices.append({
                    "index": ((movies[i]["stars"][j].lower()).find(searchTerm.lower())),
                    "type": "stars",
                    "elementOfStars": j, 
                    "lengthOfSubstring": len(searchTerm.lower()),
                    "lengthOfString": len(movies[i]["name"].lower()),
                    "searchTerm": searchTerm
                    })


    
    
    # add new entry to array with 
    # a new id and the name the user sent in JSON

    #send back the WHOLE array of data, so the client can redisplay it
    return render_template('search.html', movies = movies, data = searchResults, indices = indices) 


@application.route('/search/', methods=['GET', 'POST'])
def searchEmpty(searchterm = None):
    
    global movies 
    global searchResults
    global searchTerm
    searchResults = []

    searchTerm = ""

    for i in range (0,len(movies)):
        if searchTerm.lower() in movies[i]["name"].lower():
            searchResults.append(movies[i])

        else:
            for j in range (0,len(movies[i]["stars"])):
                if searchTerm.lower() in movies[i]["stars"][j].lower():
                    searchResults.append(movies[i])

    
    
    # add new entry to array with 
    # a new id and the name the user sent in JSON

    #send back the WHOLE array of data, so the client can redisplay it
    return render_template('search.html', movies = movies, data = searchResults) 


if __name__ == '__main__':
   application.run(debug = True)



 
