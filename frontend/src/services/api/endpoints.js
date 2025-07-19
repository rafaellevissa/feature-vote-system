export const endpoints = {
  features: {
    list: '/api/features',
    create: '/api/features',
    get: (id) => `/api/features/${id}`,
    delete: (id) => `/api/features/${id}`,
    upvote: (id) => `/api/features/${id}/upvote`,
    removeVote: (id) => `/api/features/${id}/remove-vote`,
  },
  user: {
    votes: (userId) => `/api/user/${userId}/votes`,
  },
  health: '/api/health',
};