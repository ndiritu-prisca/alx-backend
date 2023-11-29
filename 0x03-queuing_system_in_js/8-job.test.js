import createPushNotificationsJobs from './8-job.js';
import { createQueue } from 'kue';
import { describe, it, before, after, afterEach } from 'mocha';
import { expect } from 'chai';


const queue = createQueue();

describe('createPushNotificatinsJobs', function() {
  before(function () {
    queue.testMode.enter();
  });

  afterEach(function () {
    queue.testMode.clear();
  });

  after(function () {
    queue.testMode.exit();
  });

  it('display an error message if jobs is not an array', function() {
    expect(() => createPushNotificationsJobs('job', queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('create two new jobs to the queue', function() {
    const jobs = [
      {
        phoneNumber: '4151234567',
        message: 'Test message 1'
      },
      {
        phoneNumber: '4157654321',
        message: 'Test message 2'
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
  });
});
