import kue from 'kue';

// Create an array of jobs
const jobs = [
  { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
  { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153518743', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4153538781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153118782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4153718781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4159518782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4158718781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153818782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4154318781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4151218782', message: 'This is the code 4321 to verify your account' },
];

const queue = kue.createQueue();

// Loop through the array of jobs
jobs.forEach((jobData, _index) => {
  const job = queue.create('push_notification_code_2', jobData);

  // Notification on job creation
  job.on('enqueue', () => {
    console.log(`Notification job created: ${job.id}`);
  });

  // Notification on job is completion
  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  // Notification on error
  job.on('failed', (error) => {
    console.log(`Notification job ${job.id} failed: ${error}`);
  });

  // Notification on progress
  job.on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });

  // Save the job to the queue
  job.save();
});
