# API Reference

## Overview

This document provides comprehensive documentation for the test-ia-a project API. It includes detailed information about all available endpoints, methods, parameters, and responses.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Authentication](#authentication)
3. [Base URL](#base-url)
4. [Status Codes](#status-codes)
5. [Error Handling](#error-handling)
6. [Endpoints](#endpoints)

---

## Getting Started

### Requirements

- API Key (if applicable)
- HTTP Client
- JSON support

### Rate Limiting

- Default rate limit: 1000 requests per hour per API key
- Rate limit headers are included in all responses

---

## Authentication

### API Key Authentication

All API requests require authentication using an API key passed in the header:

```
Authorization: Bearer YOUR_API_KEY
```

### Example Request

```bash
curl -X GET "https://api.example.com/v1/resource" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

---

## Base URL

All API endpoints are relative to the following base URL:

```
https://api.example.com/v1
```

---

## Status Codes

The API uses standard HTTP status codes to indicate the success or failure of requests:

| Code | Description |
|------|-------------|
| 200 | OK - Request successful |
| 201 | Created - Resource successfully created |
| 204 | No Content - Successful request with no content returned |
| 400 | Bad Request - Invalid parameters or malformed request |
| 401 | Unauthorized - Missing or invalid authentication |
| 403 | Forbidden - Authenticated but not authorized |
| 404 | Not Found - Resource does not exist |
| 409 | Conflict - Request conflicts with current state |
| 429 | Too Many Requests - Rate limit exceeded |
| 500 | Internal Server Error - Server error occurred |
| 503 | Service Unavailable - Server temporarily unavailable |

---

## Error Handling

### Error Response Format

All error responses follow this format:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable error message",
    "details": {
      "field": "Specific field information"
    }
  }
}
```

### Common Error Codes

| Code | Message | Cause |
|------|---------|-------|
| `INVALID_REQUEST` | Invalid request parameters | Missing or malformed parameters |
| `UNAUTHORIZED` | Authentication failed | Missing or invalid API key |
| `FORBIDDEN` | Access denied | Insufficient permissions |
| `NOT_FOUND` | Resource not found | Invalid resource ID |
| `CONFLICT` | Resource already exists | Duplicate request |
| `RATE_LIMITED` | Rate limit exceeded | Too many requests |
| `SERVER_ERROR` | Internal server error | Unexpected server error |

---

## Endpoints

### Users

#### Get User Profile

**Endpoint:** `GET /users/{user_id}`

**Description:** Retrieve detailed information about a specific user.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `user_id` | string | Yes | The unique identifier of the user |

**Response (200 OK):**

```json
{
  "id": "user_123",
  "username": "john_doe",
  "email": "john@example.com",
  "created_at": "2025-01-01T00:00:00Z",
  "updated_at": "2026-01-04T16:54:36Z",
  "profile": {
    "first_name": "John",
    "last_name": "Doe",
    "avatar_url": "https://example.com/avatar.jpg",
    "bio": "Software Developer"
  },
  "status": "active"
}
```

**Example Request:**

```bash
curl -X GET "https://api.example.com/v1/users/user_123" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

#### Create User

**Endpoint:** `POST /users`

**Description:** Create a new user account.

**Request Body:**

```json
{
  "username": "jane_doe",
  "email": "jane@example.com",
  "password": "secure_password",
  "profile": {
    "first_name": "Jane",
    "last_name": "Doe"
  }
}
```

**Response (201 Created):**

```json
{
  "id": "user_456",
  "username": "jane_doe",
  "email": "jane@example.com",
  "created_at": "2026-01-04T16:54:36Z",
  "status": "active"
}
```

**Example Request:**

```bash
curl -X POST "https://api.example.com/v1/users" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "jane_doe",
    "email": "jane@example.com",
    "password": "secure_password"
  }'
```

---

#### Update User

**Endpoint:** `PATCH /users/{user_id}`

**Description:** Update user information.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `user_id` | string | Yes | The unique identifier of the user |

**Request Body:**

```json
{
  "email": "newemail@example.com",
  "profile": {
    "bio": "Updated bio"
  }
}
```

**Response (200 OK):**

```json
{
  "id": "user_123",
  "username": "john_doe",
  "email": "newemail@example.com",
  "updated_at": "2026-01-04T16:54:36Z"
}
```

---

#### Delete User

**Endpoint:** `DELETE /users/{user_id}`

**Description:** Delete a user account.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `user_id` | string | Yes | The unique identifier of the user |

**Response (204 No Content):**

No response body.

---

### Resources

#### List Resources

**Endpoint:** `GET /resources`

**Description:** Retrieve a paginated list of resources.

**Query Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `page` | integer | No | Page number (default: 1) |
| `per_page` | integer | No | Items per page (default: 20, max: 100) |
| `sort` | string | No | Sort field (default: created_at) |
| `order` | string | No | Sort order: asc or desc (default: desc) |

**Response (200 OK):**

```json
{
  "data": [
    {
      "id": "resource_1",
      "name": "Resource One",
      "type": "document",
      "created_at": "2025-12-01T00:00:00Z",
      "updated_at": "2026-01-04T16:54:36Z",
      "owner_id": "user_123"
    },
    {
      "id": "resource_2",
      "name": "Resource Two",
      "type": "image",
      "created_at": "2025-12-02T00:00:00Z",
      "updated_at": "2026-01-04T16:54:36Z",
      "owner_id": "user_123"
    }
  ],
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 2,
    "total_pages": 1
  }
}
```

**Example Request:**

```bash
curl -X GET "https://api.example.com/v1/resources?page=1&per_page=20" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

#### Get Resource

**Endpoint:** `GET /resources/{resource_id}`

**Description:** Retrieve detailed information about a specific resource.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_id` | string | Yes | The unique identifier of the resource |

**Response (200 OK):**

```json
{
  "id": "resource_1",
  "name": "Resource One",
  "type": "document",
  "description": "A sample resource",
  "created_at": "2025-12-01T00:00:00Z",
  "updated_at": "2026-01-04T16:54:36Z",
  "owner_id": "user_123",
  "metadata": {
    "size": 1024,
    "format": "pdf"
  }
}
```

---

#### Create Resource

**Endpoint:** `POST /resources`

**Description:** Create a new resource.

**Request Body:**

```json
{
  "name": "New Resource",
  "type": "document",
  "description": "A new resource",
  "metadata": {
    "format": "json"
  }
}
```

**Response (201 Created):**

```json
{
  "id": "resource_3",
  "name": "New Resource",
  "type": "document",
  "created_at": "2026-01-04T16:54:36Z",
  "owner_id": "user_123"
}
```

---

#### Update Resource

**Endpoint:** `PATCH /resources/{resource_id}`

**Description:** Update a resource.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_id` | string | Yes | The unique identifier of the resource |

**Request Body:**

```json
{
  "name": "Updated Resource Name",
  "description": "Updated description"
}
```

**Response (200 OK):**

```json
{
  "id": "resource_1",
  "name": "Updated Resource Name",
  "updated_at": "2026-01-04T16:54:36Z"
}
```

---

#### Delete Resource

**Endpoint:** `DELETE /resources/{resource_id}`

**Description:** Delete a resource.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `resource_id` | string | Yes | The unique identifier of the resource |

**Response (204 No Content):**

No response body.

---

### Data Operations

#### Batch Operations

**Endpoint:** `POST /batch`

**Description:** Perform multiple operations in a single request.

**Request Body:**

```json
{
  "operations": [
    {
      "method": "GET",
      "path": "/users/user_123"
    },
    {
      "method": "GET",
      "path": "/resources/resource_1"
    }
  ]
}
```

**Response (200 OK):**

```json
{
  "results": [
    {
      "status": 200,
      "data": {
        "id": "user_123",
        "username": "john_doe"
      }
    },
    {
      "status": 200,
      "data": {
        "id": "resource_1",
        "name": "Resource One"
      }
    }
  ]
}
```

---

## Rate Limiting

Response headers include rate limiting information:

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1704379476
```

---

## Pagination

List endpoints support cursor-based pagination:

**Query Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `page` | integer | Page number (default: 1) |
| `per_page` | integer | Items per page (default: 20) |

**Response Structure:**

```json
{
  "data": [...],
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 100,
    "total_pages": 5
  }
}
```

---

## Best Practices

1. **Always use HTTPS** - Never send API requests over unencrypted connections
2. **Keep API Keys Secure** - Store keys in environment variables, never commit to version control
3. **Implement Retry Logic** - Use exponential backoff for rate limit handling
4. **Handle Errors Gracefully** - Always check status codes and error messages
5. **Cache Responses** - Reduce API calls by caching when appropriate
6. **Use Pagination** - Always paginate list results for better performance

---

## Support

For API support and additional documentation, visit:
- **Documentation:** https://docs.example.com
- **Status Page:** https://status.example.com
- **Support Email:** support@example.com

---

**Document Last Updated:** 2026-01-04 16:54:36 UTC
