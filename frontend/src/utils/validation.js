export const validation = {
  required: (value, fieldName = 'Field') => {
    if (!value || value.toString().trim() === '') {
      return `${fieldName} is required`;
    }
    return null;
  },
  
  minLength: (value, min, fieldName = 'Field') => {
    if (value && value.toString().length < min) {
      return `${fieldName} must be at least ${min} characters`;
    }
    return null;
  },
  
  maxLength: (value, max, fieldName = 'Field') => {
    if (value && value.toString().length > max) {
      return `${fieldName} must be no more than ${max} characters`;
    }
    return null;
  },
  
  email: (value, fieldName = 'Email') => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (value && !emailRegex.test(value)) {
      return `${fieldName} is not valid`;
    }
    return null;
  },
};

export const validateFeature = (data) => {
  const errors = {};
  
  const titleError = validation.required(data.title, 'Title') || 
                    validation.minLength(data.title, 3, 'Title') ||
                    validation.maxLength(data.title, 200, 'Title');
  if (titleError) errors.title = titleError;
  
  const authorError = validation.required(data.author, 'Author') ||
                     validation.minLength(data.author, 2, 'Author') ||
                     validation.maxLength(data.author, 100, 'Author');
  if (authorError) errors.author = authorError;
  
  if (data.description) {
    const descError = validation.maxLength(data.description, 1000, 'Description');
    if (descError) errors.description = descError;
  }
  
  return {
    isValid: Object.keys(errors).length === 0,
    errors,
  };
};