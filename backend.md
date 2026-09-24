Part A — Authentication
Password hashing
Argon2 vs bcrypt
Register/login flow
JWT
Access tokens
Token expiration
Refresh tokens
Refresh-token rotation
Logout/revocation

Part B — Authorization
Authentication vs authorization
RBAC
Permissions
Resource ownership
Role/permission checks - Done till here 

Part C — OAuth
OAuth2 concepts
OpenID Connect
Google Login

Part D — API Security
SQL Injection
XSS
CSRF
CORS
SSRF
Broken authentication
Broken authorization
Rate limiting
Sensitive data exposure
Insecure deserialization
Security headers
Secrets management




Phase 1 — Web & Computer Science Foundations

This is one area I'd strengthen significantly.

HTTP

You need to genuinely understand:

Request/response
HTTP methods
Status codes
Headers
Cookies
Sessions
JSON
Query parameters
Path parameters
Request body
Content-Type
Authentication headers
CORS
HTTPS/TLS basics
HTTP/1.1 vs HTTP/2 basics
REST
Resource-oriented design
Idempotency
Statelessness
Pagination
Filtering
Sorting
Versioning
Error responses
Networking basics

You don't need CCNA-level networking.

But understand:

DNS
IP
TCP
Ports
TLS
Reverse proxy
Load balancer
localhost
NAT
connection lifecycle
Git
branching
merging
rebasing
pull requests
resolving conflicts
.gitignore
conventional commits
GitHub workflow

Phase 2 — FastAPI Fundamentals

Now FastAPI.

Learn
Application structure
Routers
Path parameters
Query parameters
Request bodies
Response models
Pydantic v2
Validation
Dependencies
Dependency injection
Middleware
Exception handlers
Lifespan events
Background tasks
Headers
Cookies
File uploads
CORS
OpenAPI
Swagger/ReDoc

And critically:

async def vs def

Don't memorize:

"FastAPI = async."

That's simplistic.

FastAPI itself supports both. The important thing is understanding whether the work you're doing is blocking or async-capable. The official documentation explicitly distinguishes async libraries from blocking libraries and explains when normal def is appropriate.

You should be able to explain:

request
   ↓
FastAPI
   ↓
dependency
   ↓
database/API call
   ↓
response

and what happens when that operation blocks.

Phase 3 — SQL + PostgreSQL

This should come before you become heavily dependent on an ORM.

This is one of my biggest changes to your roadmap.

SQL

Learn properly:

SELECT
INSERT
UPDATE
DELETE
WHERE
ORDER BY
GROUP BY
HAVING
JOINs
subqueries
CTEs
aggregates
constraints
primary keys
foreign keys
unique constraints
indexes
transactions
isolation levels
ACID
locks
normalization

Then:

PostgreSQL

Learn:

schema design
indexes
EXPLAIN
EXPLAIN ANALYZE
transactions
JSON/JSONB
arrays
full-text search basics
connection limits
query optimization

PostgreSQL is an excellent choice here. It remains one of the most desired database technologies in the 2025 Stack Overflow survey.

Phase 4 — SQLAlchemy + Alembic

Now ORM.

SQLAlchemy 2.x

Learn:

Engine
Sessions
Models
relationships
select()
joins
eager/lazy loading
transactions
async sessions
connection pooling
Alembic
migrations
upgrade
downgrade
migration conflicts
schema evolution

And one rule:

You should be able to write SQL without SQLAlchemy.

Otherwise you're not learning databases. You're learning which buttons to press on an abstraction layer.

Phase 5 — Build Your First Serious Backend

At this point, stop consuming tutorials.

Build something.

For example:

Project 1: Task Management API

Features:

users
authentication
projects
tasks
CRUD
PostgreSQL
SQLAlchemy
Alembic
pagination
filtering
sorting
validation
proper HTTP errors
tests
Docker

This project should teach you more than another 40-hour course.

Phase 6 — Authentication & Security

Your original roadmap is good here, but I'd expand it.

Authentication
password hashing
Argon2/bcrypt
JWT
access tokens
refresh tokens
token expiration
token rotation
logout/revocation strategies
OAuth
OAuth2 concepts
OpenID Connect
Google login
Authorization
RBAC
permissions
resource ownership
role/permission checks
Security

You should understand:

SQL injection
XSS
CSRF
CORS
SSRF
broken authentication
broken authorization
rate limiting
sensitive data exposure
insecure deserialization
security headers
secrets management

Don't just memorize OWASP names. Be able to explain how an attack happens and how your API prevents it.

Phase 7 — Redis + Background Jobs

Now Redis.

Learn:

caching
TTL
cache invalidation
Redis data structures
rate limiting
distributed locks basics
sessions

Then background processing.

I'd change your original roadmap slightly here.

Don't immediately marry yourself to:

Celery + Redis/RabbitMQ

Learn the concept first:

API
 ↓
Queue
 ↓
Worker
 ↓
Job

Then implement it using a real tool.

Understand:

retries
dead-letter queues
idempotency
delayed jobs
job failure
at-least-once delivery
duplicate processing

Celery is useful, but message queues themselves are the important concept.

Phase 8 — Testing

I'd move serious testing earlier.

Don't wait until Phase 6.

You should test throughout the entire journey.

Learn:

pytest
unit tests
fixtures
parametrization
mocking
test organization
FastAPI testing
TestClient
async tests
dependency overrides
authentication tests
Database testing
test database
transactions
migrations
integration tests

Eventually:

Unit tests
    +
Integration tests
    +
API tests

And CI runs them automatically.

Phase 9 — Architecture

Now architecture starts making sense.

Learn:

Router
   ↓
Service
   ↓
Repository
   ↓
Database

But don't turn this into religious architecture.

You don't need 47 interfaces for a CRUD app.

Learn:

separation of concerns
dependency inversion
modular design
domain boundaries
DTO/schema separation
service layer
repository pattern
configuration management
project structure

Then understand:

Monolith
Modular monolith
Microservices

And this is important:

You should probably build a modular monolith before building microservices.

Microservices are not a seniority achievement badge. They're distributed systems with additional opportunities to ruin your Tuesday.

Phase 10 — Distributed Systems

This is the biggest missing piece in your original roadmap.

For a serious backend engineer, learn:

horizontal scaling
load balancing
stateless services
caching
replication
partitioning
queues
eventual consistency
distributed locks
idempotency
retries
timeouts
circuit breakers
rate limiting
CAP theorem
consistency models
database replication
sharding basics

You don't need to become a distributed systems researcher.

But you should be able to reason about:

"What happens when 100,000 users hit this endpoint simultaneously?"

That is backend engineering.

Phase 11 — Docker + Linux

I'd actually move Docker earlier than your roadmap does.

Current industry data strongly supports this. Docker saw a particularly large increase in adoption in the 2025 Stack Overflow survey, and current backend job data consistently puts Docker, AWS and Kubernetes among commonly requested infrastructure skills.

Learn:

Linux
filesystem
permissions
processes
ports
environment variables
SSH
logs
curl
grep
ps
top
kill
Docker
images
containers
Dockerfile
volumes
networks
environment variables
Docker Compose
multi-stage builds
container health checks

Eventually:

FastAPI
PostgreSQL
Redis
Worker

all running locally through Docker Compose.

Phase 12 — CI/CD

Learn:


GitHub Actions

Pipeline:

Push
 ↓
Lint
 ↓
Type check
 ↓
Tests
 ↓
Build Docker image
 ↓
Deploy

Also learn:

secrets
environment variables
staging vs production
migrations during deployment
rollback basics
Phase 13 — Cloud

Start simple.

First

Deploy to something easy.

Understand:

DNS
domain
HTTPS
environment variables
logs
databases
networking

Then AWS.

AWS fundamentals
EC2
ECS
RDS
S3
IAM
VPC
CloudWatch
ALB
ECR

You don't need to learn every AWS service because AWS has apparently decided that naming 200 services is a reasonable user experience.

Phase 14 — Observability

Your original roadmap has this, but I'd make it more serious.

Learn:

Logging

Structured logs:

{
  "request_id": "...",
  "user_id": "...",
  "endpoint": "/orders",
  "status": 500,
  "duration_ms": 421
}
Metrics
request count
latency
error rate
CPU
memory
DB connections
Tracing

Understand:

Request
 ↓
API
 ↓
Service
 ↓
Database
 ↓
Redis

and how to trace latency across the chain.

Learn the basic OpenTelemetry model too.

Phase 15 — Performance

Now performance.

Learn:

database indexes
query optimization
connection pooling
N+1 queries
caching
async I/O
pagination
batching
profiling
load testing

Tools:

EXPLAIN ANALYZE
Locust
k6
profiling tools

But don't prematurely optimize.

First make it correct.

Then measure.

Then optimize.

Phase 16 — Real-Time Systems

Now:

WebSockets

Learn:

connection lifecycle
authentication
broadcasting
rooms
reconnects
scaling WebSockets

Then build something like:

Real-time chat

This teaches you things a normal REST API won't.

Phase 17 — Kafka / Event Streaming

I'd add this to your roadmap.

You don't necessarily need Kafka for your first job, but understanding event-driven architecture becomes valuable as you move toward stronger backend roles. Current backend job datasets frequently mention Kafka alongside distributed systems and microservices.

Learn:

producers
consumers
topics
partitions
offsets
consumer groups
ordering
delivery semantics
event-driven architecture

Don't spend three months becoming Kafka's unpaid intern.

Phase 18 — System Design

Start basic system design before you're job hunting.

Learn progressively:

Level 1

Design:

URL shortener
task manager
chat app
file upload service
Level 2

Understand:

scaling
caching
queues
databases
load balancers
replication
Level 3

Design:

Instagram-like feed
notification system
payment system
video processing system
ride-sharing backend

You'll gradually learn to reason about tradeoffs instead of reciting architecture diagrams you found five minutes before the interview.

Phase 19 — Portfolio

Your original:

2–3 solid FastAPI projects

is correct.

But quality matters enormously more than quantity.

I'd want:

Project 1 — Production-style SaaS API

Example:

Project Management SaaS

FastAPI
PostgreSQL
SQLAlchemy
Alembic
Redis
JWT
RBAC
Docker
pytest
GitHub Actions
AWS
logging
monitoring
Project 2 — Real-time system

Example:

Chat / Collaboration platform

FastAPI
WebSockets
PostgreSQL
Redis
background workers
Docker
CI/CD
AWS
Project 3 — Distributed/event-driven system

Example:

Order + payment + notification system

API
 ↓
PostgreSQL
 ↓
Kafka
 ↓
Workers
 ↓
Notification service

This one demonstrates that you understand backend architecture rather than simply knowing FastAPI decorators.