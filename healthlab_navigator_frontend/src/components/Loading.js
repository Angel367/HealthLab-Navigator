import React from 'react';

function Loading() {
  return (
    <div className="d-flex align-items-center">
      <div className="spinner-border text-primary" role="status">
        <span className="visually-hidden">Loading...</span>
      </div>
      <span className="ms-2">Загрузка...</span>
    </div>
  );
}

export default Loading;

