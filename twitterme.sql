--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2 (Ubuntu 13.2-1.pgdg18.04+1)
-- Dumped by pg_dump version 13.2 (Ubuntu 13.2-1.pgdg18.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: follows; Type: TABLE; Schema: public; Owner: amit
--

CREATE TABLE public.follows (
    follower_id integer,
    followed_id integer
);


ALTER TABLE public.follows OWNER TO amit;

--
-- Name: likes; Type: TABLE; Schema: public; Owner: amit
--

CREATE TABLE public.likes (
    user_id integer,
    post_id integer
);


ALTER TABLE public.likes OWNER TO amit;

--
-- Name: post; Type: TABLE; Schema: public; Owner: amit
--

CREATE TABLE public.post (
    id integer NOT NULL,
    date_posted timestamp without time zone NOT NULL,
    content text NOT NULL,
    user_id integer NOT NULL,
    retweet integer,
    comment integer
);


ALTER TABLE public.post OWNER TO amit;

--
-- Name: post_id_seq; Type: SEQUENCE; Schema: public; Owner: amit
--

CREATE SEQUENCE public.post_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.post_id_seq OWNER TO amit;

--
-- Name: post_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: amit
--

ALTER SEQUENCE public.post_id_seq OWNED BY public.post.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: amit
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    username character varying(25) NOT NULL,
    email character varying(120) NOT NULL,
    image_file character varying(20),
    password character varying(64) NOT NULL,
    verified integer
);


ALTER TABLE public."user" OWNER TO amit;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: amit
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO amit;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: amit
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: post id; Type: DEFAULT; Schema: public; Owner: amit
--

ALTER TABLE ONLY public.post ALTER COLUMN id SET DEFAULT nextval('public.post_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: amit
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Data for Name: follows; Type: TABLE DATA; Schema: public; Owner: amit
--

COPY public.follows (follower_id, followed_id) FROM stdin;
3	23
25	23
27	23
29	23
31	23
33	23
35	23
37	23
6	37
24	37
26	37
28	37
30	37
32	37
34	37
36	37
\.


--
-- Data for Name: likes; Type: TABLE DATA; Schema: public; Owner: amit
--

COPY public.likes (user_id, post_id) FROM stdin;
23	36
23	34
23	32
23	28
23	24
23	20
\.


--
-- Data for Name: post; Type: TABLE DATA; Schema: public; Owner: amit
--

COPY public.post (id, date_posted, content, user_id, retweet, comment) FROM stdin;
1	2021-04-25 15:25:52.119563	Hello hermione here, I like TweetMe..!	24	\N	\N
2	2021-04-25 15:26:57.14178	Hello, amit032 here, I like TweetMe..!	3	\N	\N
3	2021-04-25 15:27:38.077799	Hello, amit032 here, I like TweetMe..!	3	\N	\N
4	2021-04-25 15:27:38.112018	Hello, shreyas here, I like TweetMe..!	6	\N	\N
5	2021-04-25 15:27:38.144224	Hello, tejas2904 here, I like TweetMe..!	23	\N	\N
6	2021-04-25 15:27:38.166529	Hello, hermione here, I like TweetMe..!	24	\N	\N
7	2021-04-25 15:27:38.203357	Hello, snape here, I like TweetMe..!	25	\N	\N
8	2021-04-25 15:27:38.239224	Hello, dumbledore here, I like TweetMe..!	26	\N	\N
9	2021-04-25 15:27:38.274626	Hello, harry here, I like TweetMe..!	27	\N	\N
10	2021-04-25 15:27:38.294514	Hello, ron here, I like TweetMe..!	28	\N	\N
11	2021-04-25 15:27:38.313398	Hello, lily here, I like TweetMe..!	29	\N	\N
12	2021-04-25 15:27:38.325512	Hello, draco here, I like TweetMe..!	30	\N	\N
13	2021-04-25 15:27:38.357466	Hello, voldemort here, I like TweetMe..!	31	\N	\N
14	2021-04-25 15:27:38.391014	Hello, lovegood here, I like TweetMe..!	32	\N	\N
15	2021-04-25 15:27:38.422389	Hello, hagrid here, I like TweetMe..!	33	\N	\N
16	2021-04-25 15:27:38.459406	Hello, paralta here, I like TweetMe..!	34	\N	\N
17	2021-04-25 15:27:38.489845	Hello, santiago here, I like TweetMe..!	35	\N	\N
18	2021-04-25 15:27:38.521378	Hello, boyle here, I like TweetMe..!	36	\N	\N
19	2021-04-25 15:27:38.54613	Hello, siddhi here, I like TweetMe..!	37	\N	\N
20	2021-04-25 15:29:28.886823	I am amit032, interested in flask 😊..!	3	\N	\N
21	2021-04-25 15:29:28.920598	I am shreyas, interested in flask 😊..!	6	\N	\N
22	2021-04-25 15:29:28.955305	I am tejas2904, interested in flask 😊..!	23	\N	\N
23	2021-04-25 15:29:28.980599	I am hermione, interested in flask 😊..!	24	\N	\N
24	2021-04-25 15:29:29.016278	I am snape, interested in flask 😊..!	25	\N	\N
25	2021-04-25 15:29:29.033941	I am dumbledore, interested in flask 😊..!	26	\N	\N
26	2021-04-25 15:29:29.052968	I am harry, interested in flask 😊..!	27	\N	\N
27	2021-04-25 15:29:29.0641	I am ron, interested in flask 😊..!	28	\N	\N
28	2021-04-25 15:29:29.076268	I am lily, interested in flask 😊..!	29	\N	\N
29	2021-04-25 15:29:29.08663	I am draco, interested in flask 😊..!	30	\N	\N
30	2021-04-25 15:29:29.098334	I am voldemort, interested in flask 😊..!	31	\N	\N
31	2021-04-25 15:29:29.108311	I am lovegood, interested in flask 😊..!	32	\N	\N
32	2021-04-25 15:29:29.119362	I am hagrid, interested in flask 😊..!	33	\N	\N
33	2021-04-25 15:29:29.131676	I am paralta, interested in flask 😊..!	34	\N	\N
34	2021-04-25 15:29:29.143258	I am santiago, interested in flask 😊..!	35	\N	\N
35	2021-04-25 15:29:29.152619	I am boyle, interested in flask 😊..!	36	\N	\N
36	2021-04-25 15:29:29.166102	I am siddhi, interested in flask 😊..!	37	\N	\N
37	2021-04-25 17:13:22.558104	@boyle  abcd	23	\N	35
38	2021-04-25 17:13:37.767098	@amit032  Hello	23	\N	20
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: amit
--

COPY public."user" (id, username, email, image_file, password, verified) FROM stdin;
3	amit032	b@gmail.com	default.jpg	abc@123	0
6	shreyas	shreyas@gmail.com	default.jpg	abc@123	0
23	tejas2904	tejas2904@gmail.com	default.jpg	abc@123	0
24	hermione	hermione@gmail.com	default.jpg	abc@123	0
25	snape	snape@gmail.com	default.jpg	abc@123	0
26	dumbledore	dumbledore@gmail.com	default.jpg	abc@123	0
27	harry	harry@gmail.com	default.jpg	abc@123	0
28	ron	ron@gmail.com	default.jpg	abc@123	0
29	lily	lily@gmail.com	default.jpg	abc@123	0
30	draco	draco@gmail.com	default.jpg	abc@123	0
31	voldemort	voldemort@gmail.com	default.jpg	abc@123	0
32	lovegood	lovegood@gmail.com	default.jpg	abc@123	0
33	hagrid	hagrid@gmail.com	default.jpg	abc@123	0
34	paralta	paralta@gmail.com	default.jpg	abc@123	0
35	santiago	santiago@gmail.com	default.jpg	abc@123	0
36	boyle	boyle@gmail.com	default.jpg	abc@123	0
37	siddhi	siddhi@gmail.com	default.jpg	abc@123	0
\.


--
-- Name: post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: amit
--

SELECT pg_catalog.setval('public.post_id_seq', 38, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: amit
--

SELECT pg_catalog.setval('public.user_id_seq', 37, true);


--
-- Name: post post_pkey; Type: CONSTRAINT; Schema: public; Owner: amit
--

ALTER TABLE ONLY public.post
    ADD CONSTRAINT post_pkey PRIMARY KEY (id);


--
-- Name: user user_email_key; Type: CONSTRAINT; Schema: public; Owner: amit
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_email_key UNIQUE (email);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: amit
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: user user_username_key; Type: CONSTRAINT; Schema: public; Owner: amit
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_username_key UNIQUE (username);


--
-- Name: follows follows_followed_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: amit
--

ALTER TABLE ONLY public.follows
    ADD CONSTRAINT follows_followed_id_fkey FOREIGN KEY (followed_id) REFERENCES public."user"(id);


--
-- Name: follows follows_follower_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: amit
--

ALTER TABLE ONLY public.follows
    ADD CONSTRAINT follows_follower_id_fkey FOREIGN KEY (follower_id) REFERENCES public."user"(id);


--
-- Name: likes likes_post_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: amit
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_post_id_fkey FOREIGN KEY (post_id) REFERENCES public.post(id);


--
-- Name: likes likes_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: amit
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- Name: post post_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: amit
--

ALTER TABLE ONLY public.post
    ADD CONSTRAINT post_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- PostgreSQL database dump complete
--

