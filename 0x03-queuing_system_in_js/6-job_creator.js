import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '0112345678',
  message: 'Hello, this is a notification!',
};

const job = queue.create('push_notification_code', jobData);

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  } else {
    console.error('Error creating notification job:', err);
  }
});
