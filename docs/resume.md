Title: Résumé: Heungsub Lee

Heungsub Lee
============

Email {: .label }
: [heungsub.lee@subl.ee](mailto:heungsub.lee@subl.ee)
  {: .attr }

Web Sites {: .label }
: [Homepage](/),
  [GitHub Profile](https://github.com/sublee),
  [LinkedIn Profile](https://linkedin.com/in/sublee)
  {: .attr }
{^ .attrs }

---

Interests
---------

- Distributed server architecture on a cloud infrastructure
- DevOps in huge systems
- High quality internationalization systems based on linguistics
- Efficient and happy development process
- Free and open source software

Skills
------

Programming Languages {: .label }
: Go, Python (expert), Bash, C#, Node.js, C
  {: .attr }

Back-end Technologies {: .label }
: ZeroMQ, Couchbase, Redis, etcd, MySQL, PostgreSQL
  {: .attr }

Web Development {: .label }
: Vue.js, Lodash, Flask, jQuery, socket.io, HTML5/CSS3, Nginx
  {: .attr }

DevOps {: .label }
: AWS, Terraform, Google Cloud, Docker, Ansible, systemd, Linux
  {: .attr }

Test Engineering {: .label }
: Testify, pytest, GitLab CI, Travis CI
  {: .attr }

Tools {: .label }
: Vim, tmux, ZSH, Visual Studio Code, Git, VirtualBox
  {: .attr }
{^ .attrs }

---

Work Experience
---------------

Game Server Technical Director {: .label }
What! Studio in [Nexon][], 2013--
:   Developing <cite>[Durango][]</cite>, a seamless open world MMORPG.
    {: .note }

:   Designing and implementing the architecture of a distributed MMORPG server.
    Achieved up to 70k concurrent users per MMO world with a scalable
    geological space. Launched this game in Korea and Indonesia. Maintaining
    the game service continuously.

    Built an internationalization system based on gettext. Implemented a high
    quality message interpolation focused on linguistics features of Korean and
    Indo-European languages.

    Using Python, C#, Cython, ZeroMQ, MsgPack, Couchbase, etcd, Redis, MySQL,
    Unity3D, Git, PlasticSCM, Ansible, Fabric, Docker, Ubuntu, and AWS.

Game Development Engineer {: .label }
Team Lupin in [Nexon][], 2011--2013
:   Developed and published mobile and Web series of
    <cite>[KartRider][]</cite>, a synchronous multiplayer casual racing game.
    {: .note }

:   Designed and implemented a distributed game server architecture for
    synchronous multiplayer games for the <cite>KartRider Dash</cite> and
    <cite>KartRider Coin Rush</cite> series. Launched these games globally and
    maintained them.

    Researched various rating systems such as [Elo][], [Glicko][], and
    [TrueSkill][]. Implemented a simple matchmaker for 4v4 or free-for-all
    racing games.

    Used Python, Redis as a message broker, Couchbase, MongoDB, Unity3D,
    Mercurial, Ubuntu, and AWS.

Full Stack Web Developer {: .label }
[Npine][], 2008--2011
:   Supplies stock images for business on <cite>[Iclickart][]</cite>.
    {: .note }

:   Developed a web server framework adapting the MVC pattern by PHP5. Made
    and maintained web sites where provide stock images including
    <cite>[Iclickart][]</cite> by the own framework. Maintained physical Linux
    machines in a data center.

    Led the software engineering team.

Front-end Web Developer {: .label }
[Lunant][], 2008--2011
:   Served <cite>VLAAH</cite>, a social network service for discovering,
    sharing, and utilizing opinions.
    {: .note }

:   Designed and implemented the UI/UX for <cite>VLAAH</cite> by PHP5,
    JavaScript with MooTools, and Python.

    Developed [jDoctest][], which tests JavaScript examples in doc comments,
    by JavaScript.

Open Source Experience
----------------------

[Hangulize 2][hangulize2], 2018--
:   Reboot of [Hangulize][] in Go.
    {: .note }

:   Re-implemented Hangulize, which is also listed at the below, to achieve
    better features, performance, and productivity in Go rather than Python.

[Profiling][], 2014--
:   An interactive profiler for Python inspired by the Unity3D profiler.
    {: .note }

:   Developed to find bottlenecks in the <cite>[Durango][]</cite> server by
    Python and C. Designed a handy interactive TUI like [htop][] by [Urwid][].

    On GitHub, 2700+ people stared this project. Also it was the 3rd daily
    trending repository at Sep 22, 2014.

[TrueSkill][trueskill-py], 2012--
:   A Python implementation of [TrueSkill<sup>TM</sup>][trueskill] which is a
    rating algorithm for Xbox Live.
    {: .note }

:   Implemented TrueSkill<sup>TM</sup> by Python with simple API to learn and
    share the smart algorithm.

[Hangulize][], 2010--
:   Automatically transcribes a non-Korean word into Hangul.
    {: .note }

:   Implemented the library to realize [Brian Jongseong Park's idea]
    [hangulize-idea] by Python and complex regular expressions.

    Designed and implemented the Web service and RESTful API by [Flask][] on
    [Google App Engine][gae]. Many professional Korean translators visit here
    to translate undocumented proper nouns.

Others
:   - [Zeronimo][] -- A distributed RPC system based on ZeroMQ
    - [Lets][] -- Several utilities for gevent
    - [Energy][] -- Energy system for social games
    - [Flask-AutoIndex][] -- mod_autoindex for Flask
    - [SUBLEERUNKER][] -- A simple prody game of SUBERUNKER
    - [Me2virus][] -- An XSS attack on [Me2day][], a social network service.
                      When a user looks an infected post, a new infected post
                      was written on the user's wall.

Contributed
:   [Babel#427](https://github.com/python-babel/babel/pull/427),
    [#488](https://github.com/python-babel/babel/pull/488);
    [couchbase-python-client#32](
      https://github.com/couchbase/couchbase-python-client/pull/32),
    [#33](https://github.com/couchbase/couchbase-python-client/pull/33),
    [#35](https://github.com/couchbase/couchbase-python-client/pull/35);
    [etcd#4320](https://github.com/coreos/etcd/pull/4320);
    [Flask-0.10.1](https://github.com/mitsuhiko/flask/commit/6fca662);
    [gevent#608](https://github.com/gevent/gevent/pull/608);
    [jQuery-1.4.3](https://blog.jquery.com/2010/10/16/jquery-143-released/);
    [node-irc#3](https://github.com/martynsmith/node-irc/pull/3);
    [pytest-rerunfailures#47](
      https://github.com/pytest-dev/pytest-rerunfailures/pull/47);
    [PyZMQ#951](https://github.com/zeromq/pyzmq/pull/951).

Invited Talks
-------------

- [The server architecture of Durango Vol. 3][ndc18] at NDC 2018 (Korean)
- [Python Survival Guide][nxtk16] at Nexon Talk 2016 (Korean)
- [The server architecture of Durango Vol. 2][ndc16] at NDC 2016 (Korean)
- [Profiling][pycon15] at PyCon KR 2015 (Korean)
- [The server architecture of Durango][ndc14] at NDC 2014 (Korean)

[ndc18]: https://subl.ee/~ndc18
[ndc16]: https://subl.ee/~ndc16
[ndc14]: https://subl.ee/~ndc14

[nxtk16]:  https://subl.ee/~nxtk16
[pycon15]: https://subl.ee/~pycon15

Education
---------

Computer Software, [Kwangwoon University][kw], 2008
-- Completed the first year and left in mid course.

[profiling]: https://github.com/what-studio/profiling
[htop]: http://hisham.hm/htop
[urwid]: http://urwid.org/
[trueskill-py]: http://trueskill.org/
[trueskill]: http://research.microsoft.com/en-us/projects/trueskill/
[hangulize2]: https://github.com/sublee/hangulize2
[hangulize]: http://hangulize.org/
[hangulize-idea]: http://iceager.egloos.com/2610028
[energy]: http://pythonhosted.org/energy
[flask-autoindex]: http://pythonhosted.org/Flask-AutoIndex
[zeronimo]: https://github.com/sublee/zeronimo
[lets]: https://github.com/sublee/lets
[jdoctest]: https://lunant.github.com/jdoctest
[subleerunker]: /runker/
[me2virus]: https://github.com/sublee/me2virus
[me2day]: http://en.wikipedia.org/wiki/Me2day
[flask]: http://flask.pocoo.org/
[gae]: https://cloud.google.com/appengine
[nexon]: http://company.nexon.com/eng
[durango]: http://durango.nexon.com/
[vindictus]: http://en.wikipedia.org/wiki/Vindictus
[kartrider]: http://kart.nexon.com/
[elo]: http://en.wikipedia.org/wiki/Elo_rating_system
[glicko]: http://en.wikipedia.org/wiki/Glicko_rating_system
[npine]: http://en.npine.com/
[iclickart]: http://iclickart.co.kr/
[lunant]: http://lunant.net/
[kw]: http://www.kw.ac.kr/

*[MMORPG]: Massively multiplayer online role-playing game
*[MVC]: Model-view-controller
*[TUI]: Text-based User Interface
*[XSS]: Cross-site Scripting
*[NDC]: Nexon Developers Conference
