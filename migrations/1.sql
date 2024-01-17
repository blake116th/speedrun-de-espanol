CREATE TABLE words (
  id integer primary key,
  word_es text not null,
  word_en text not null,
  example_sentence_es text not null,
  example_sentence_en text not null,
  image_link text null,
  gender text check( gender IN ('M','F')) null
);
