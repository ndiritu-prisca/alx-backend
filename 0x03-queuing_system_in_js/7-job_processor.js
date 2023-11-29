import kue from 'kue';

// Create a Kue queue named push_notification_code_2 with concurrency 2
const queue = kue.createQueue({
  prefix: 'q',
  redis: {
    port: 6379,
    host: '127.0.0.1',
  },
});

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklistedNumbers.includes(phoneNumber)) {
    const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
    return done(new Error(errorMessage));
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Complete the job
  done();
}

// Process jobs from the push_notification_code_2 queue with concurrency 2
queue.process('push_notification_code_2', 2, (job, done) => {
  // Extract data from the job
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message, job, done);
});
